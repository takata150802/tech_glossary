import argparse
import base64
import logging
import os
import re
from glob import glob
from markdown_it import MarkdownIt
from markdown_it.token import Token
from markdown_it.tree import SyntaxTreeNode
from mdformat.renderer import MDRenderer

logger = logging.getLogger(__name__)
URL_PATTERN = re.compile(r'<!-- \u8a18\u4e8bURL:(.*) -->')


def setup_logging(log_level):
    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")
    logging.basicConfig(level=numeric_level)


def make_token(content: str, html: bool = False):
    return Token(
        type='html_inline' if html else 'text', tag='', nesting=0,
        attrs={}, map=None, level=0, children=None,
        content=content, markup='', info='', meta={}, block=False, hidden=False
    )


def commonpath_length(base_path: str, target_path: str) -> int:
    try:
        return len(os.path.commonpath([base_path, target_path]))
    except ValueError:
        return 0


class TechTerm:
    def __init__(self, anchor, entry_word, md_file):
        self.anchor = anchor
        self.entry_word = entry_word
        self.md_file = md_file

    def __lt__(self, other):
        return len(self.entry_word) < len(other.entry_word)


class MarkDownFile:
    def __init__(self, repo, relpath):
        self.repo = repo
        self.relpath = relpath
        self.url = self._extract_url()
        self.tech_terms, self.tokens, self.node = self._extract_tech_terms()

    def _extract_url(self):
        path = self.input_path
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        matches = re.findall(URL_PATTERN, text)
        if len(matches) != 1:
            logger.error(f"Markdown file {path} should have one article URL comment.")
            return None
        return matches[0].strip()

    def _extract_tech_terms(self):
        path = self.input_path
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        md = MarkdownIt("commonmark")
        tokens = md.parse(text)
        node = SyntaxTreeNode(tokens)
        tech_terms = []

        for h2 in [n for n in node.walk() if n.type == 'heading' and n.nester_tokens.opening.tag == 'h2']:
            for inline in [c for c in h2.walk() if c.type == 'inline']:
                anchor = base64.b64encode(inline.content.encode()).decode()
                inline.token.children.extend([make_token(f'<a id="{anchor}">', html=True), make_token('</a>', html=True)])

                for text_node in [c for c in inline.children if c.type == 'text']:
                    for entry_word in map(str.strip, text_node.content.split('|')):
                        assert entry_word not in [t.entry_word for t in tech_terms], entry_word
                        tech_terms.append(TechTerm(anchor, entry_word, self))

        tech_terms.sort(key=lambda t: len(t.entry_word), reverse=True)
        return tech_terms, node.to_tokens(), SyntaxTreeNode(node.to_tokens())

    def insert_links(self):
        self.repo.md_files.sort(key=lambda x: commonpath_length(self.relpath, x.relpath), reverse=True)
        all_terms = [t for f in self.repo.md_files for t in f.tech_terms]

        def my_node_walk(self):
            if self.type in ("heading", "link", "html_inline", "html_block", "code_inline"):
                return
            yield self
            for child in self.children:
                yield from child.my_node_walk()

        setattr(SyntaxTreeNode, "my_node_walk", my_node_walk)

        for inline in [n for n in self.node.my_node_walk() if n.type == 'inline']:
            assert all(c.map is None for c in inline.children)
            for term in all_terms:
                link = f'<a href="{term.md_file.url}{term.anchor}">'  # No "&anchor=" needed
                while True:
                    updated = False
                    new_children = []
                    inside_link = False
                    for token in inline.token.children:
                        if token.type == 'html_inline' and token.content.startswith('<a '):
                            inside_link = True
                        elif token.type == 'html_inline' and token.content == '</a>':
                            inside_link = False

                        if inside_link or term.entry_word not in token.content:
                            new_children.append(token)
                        else:
                            updated = True
                            idx = token.content.index(term.entry_word)
                            before = token.content[:idx]
                            after = token.content[idx + len(term.entry_word):]
                            new_children.extend([
                                make_token(before),
                                make_token(link, html=True),
                                make_token(term.entry_word),
                                make_token('</a>', html=True),
                                make_token(after)
                            ])
                    inline.token.children = new_children
                    if not updated:
                        break

        self.tokens = self.node.to_tokens()
        self.node = SyntaxTreeNode(self.tokens)

    def save(self):
        renderer = MDRenderer()
        output_md = renderer.render(self.tokens, {}, {})
        output_path = self.output_path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_md)

    @property
    def input_path(self):
        return os.path.join(self.repo.input_dir, self.relpath)

    @property
    def output_path(self):
        return os.path.join(self.repo.output_dir, self.relpath)


class Repository:
    def __init__(self, input_dir):
        self.input_dir = os.path.abspath(input_dir)
        self.md_files = self._load_files()

    def _load_files(self):
        pattern = os.path.join(self.input_dir, '**', '*.md')
        files = glob(pattern, recursive=True)
        relpaths = [os.path.relpath(p, self.input_dir) for p in files]
        logger.info("Found markdown files:")
        for f in files:
            logger.info(f" - {f}")
        return [MarkDownFile(self, p) for p in relpaths]

    def generate(self, output_dir):
        self.output_dir = os.path.abspath(output_dir)
        os.makedirs(self.output_dir, exist_ok=True)
        for f in self.md_files:
            f.insert_links()
            f.save()


def main():
    parser = argparse.ArgumentParser(description='Insert Anchor Links')
    parser.add_argument('--input-dir', default='input-github')
    parser.add_argument('--output-dir', default='output')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='WARNING')
    args = parser.parse_args()

    setup_logging(args.log_level)
    repo = Repository(args.input_dir)
    repo.generate(args.output_dir)


if __name__ == "__main__":
    main()

