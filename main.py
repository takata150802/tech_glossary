#!/usr/bin/env python
from markdown_it import MarkdownIt
from markdown_it.token import Token
from markdown_it.tree import SyntaxTreeNode 
from mdformat.renderer import MDRenderer
import base64
from logging import getLogger
from os import makedirs as makedirs
from os.path import abspath as abspath
from os.path import dirname as dirname
from os.path import exists as path_exists
from os.path import join as path_join
from os.path import relpath as relpath
from os.path import commonpath as commonpath
import argparse
import logging
parser = argparse.ArgumentParser(description='Inserting Anchor Link')
parser.add_argument('--input-dir', dest='input_dir', type=str, default='input-github', help='Input Directory Path')
parser.add_argument('--output-dir', dest='output_dir', type=str, default='output', help='Output Directory Path')
parser.add_argument('--log-level', dest='log_level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    default='WARNING', help='Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
args = parser.parse_args()
logger = getLogger(__name__)
numeric_level = getattr(logging, args.log_level, None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.log_level)
logging.basicConfig(level=numeric_level)
input_dir = abspath(args.input_dir)
output_dir = abspath(args.output_dir)

class Repository:
    def __init__(self, input_dir):
        self.input_dir = input_dir
        import glob
        pathname = path_join(input_dir, '**', '*.md')
        md_file_paths = glob.glob(pathname, recursive=True)
        md_file_relpaths = [relpath(p, input_dir) for p in md_file_paths]
        self.md_files = [MarkDownFile(self, p) for p in md_file_relpaths]
        logger.info("Markdown files, which this script found, are:")
        for f in md_file_paths:
            logger.info(" - " + f)
        return
    def generate(self, output_dir):
        self.output_dir = output_dir
        if not path_exists(output_dir):
            makedirs(output_dir)
        else:
            logger.warning("Directory {} is already exist.".format(output_dir))
        [ f.generate_link() for f in self.md_files]
        [ f.generate_output_md_file() for f in self.md_files]
        return

import re
re_url = re.compile(r'<!-- 記事URL:(.*) -->')
class MarkDownFile:
    def __init__(self, klass_repository, relpath):
        self.relpath = relpath
        self.repo = klass_repository
        self.url = self._re_match_url()
        self.tech_terms, self.tokens, self.node = self._generate_tech_terms()
        return
    def _generate_tech_terms(self):
        # [NOTE]: TechTermのentry_wordとanchorを取得
        path = self.get_input_file_path()
        with open(path, 'r') as f:
            text = f.read()
        md = MarkdownIt("commonmark")
        tokens = md.parse(text)
        node = SyntaxTreeNode(tokens)
        tech_terms = []
        for i in [ iii for iii in node.walk() 
                       if iii.type == 'heading' 
                       and  iii.nester_tokens.opening.tag == 'h2']:
            for inline_node  in [ iii for iii in i.walk() if iii.type == 'inline']:
                assert all([c.map == None for c in inline_node.children])
                anchor = base64.b64encode(inline_node.content.encode('utf-8')).decode('utf-8')
                atag_tokens_content = '<a id="' + anchor + '">'
                atag_tokens = [
                        Token(type='html_inline', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content=atag_tokens_content, markup='', info='', meta={}, block=False, hidden=False),
                        Token(type='html_inline', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content='</a>', markup='', info='', meta={}, block=False, hidden=False),
                        ]
                ### NOTE: The "inline_node.token.children" are Token(s) in the same file of the markdown file
                inline_node.token.children.extend(atag_tokens)
                for c in [ccc for ccc in inline_node.children if ccc.type == 'text']:
                    header_h2_text = c.content
                    for entry_word in [ i.strip() for i in header_h2_text.split('|')]:
                        ### NOTE: 同一ファイル内で同じ見出し語(h2)はNG
                        assert entry_word not in [t.entry_word for t in tech_terms], entry_word
                        t = TechTerm(anchor, entry_word, self)
                        tech_terms.append(t)
        tokens = node.to_tokens()
        ### NOTE: 見出し語の文字列長い順に並び替え
        tech_terms.sort(key=lambda x: len(x.entry_word), reverse=True)
        node = SyntaxTreeNode(tokens)
        return tech_terms, tokens, node 
    def _re_match_url(self):
        path = self.get_input_file_path()
        with open(path, 'r') as f:
            self.text = f.read()
        # [NOTE]: 記事URL(=https:~ ) の部分だけ後方参照して取り出す
        ret = re.findall(re_url, self.text)
        if len(ret) != 1:
            logger.fatal('Markdown File {} should have only one url.'.format(path))
            logger.fatal([str(ret) for ret in ret])
            return None
        else:
            logger.debug(ret[0])
            return ret[0]
    def get_input_file_path(self):
        return path_join(self.repo.input_dir, self.relpath)
    def get_output_file_path(self):
        return path_join(self.repo.output_dir, self.relpath)
    def generate_link(self):
        ### NOTE: 他のMarkDownFileをソートする。基準は、自身の.relpathとの共通部分の長さ
        self.repo.md_files.sort(key=lambda x: commonpath_length(self.relpath, x.relpath), reverse=True)
        all_tech_terms = [ t for f in self.repo.md_files for t in f.tech_terms]
        ### NOTE: markdown_it のSyntaxTreeNodeのwalk()メソッドの改造版
        ###       無視すべきnodeとその配下のnodeをskipする
        from typing import TypeVar
        from collections.abc import Generator
        _NodeType = TypeVar("_NodeType", bound="SyntaxTreeNode")
        def my_node_walk(self: _NodeType) -> Generator[_NodeType, None, None]:
            if self.type in ("heading", "link", "html_inline", "html_block", "code_inline"):
                return
            yield self
            for child in self.children:
                yield from child.my_node_walk()
        setattr(SyntaxTreeNode, my_node_walk.__name__, my_node_walk)
        for inline_node  in [ i for i in self.node.my_node_walk() if i.type == 'inline']:
            ### NOTE: The "inline_node.token.children" are Token(s) in the same file of the markdown file
            assert all([c.map == None for c in inline_node.children])
            for tech_term in all_tech_terms:
                entry_word = tech_term.entry_word
                anchor = tech_term.anchor
                url = tech_term.md_file.url
                # link_token_content = '<a href="' + url + '&anchor=' + anchor + '">'
                link_token_content = '<a href="' + url + anchor + '">'
                while True:
                    token_replaced_and_retry  = False
                    new_list_siblings  = []
                    inside_atag = False
                    for s in inline_node.token.children:
                        if s.type == "html_inline" and s.content.startswith('<a '):
                            inside_atag = True
                        elif s.type == "html_inline" and s.content == '</a>':
                            inside_atag = False
                        else:
                            pass
                        if inside_atag:
                            new_list_siblings.append(s)
                        elif entry_word in s.content:
                            token_replaced_and_retry = True
                            index = s.content.index(entry_word)
                            first_part = s.content[:index]
                            second_part = s.content[index + len(entry_word):]
                            replaced_tokens = [
                                    Token(type='text', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content=first_part, markup='', info='', meta={}, block=False, hidden=False),
                                    Token(type='html_inline', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content=link_token_content, markup='', info='', meta={}, block=False, hidden=False),
                                    Token(type='text', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content=entry_word, markup='', info='', meta={}, block=False, hidden=False),
                                    Token(type='html_inline', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content='</a>', markup='', info='', meta={}, block=False, hidden=False),
                                    Token(type='text', tag='', nesting=0, attrs={}, map=None, level=0, children=None, content=second_part,  markup='', info='', meta={}, block=False, hidden=False),
                                    ]
                            new_list_siblings.extend(replaced_tokens)
                        else:
                            new_list_siblings.append(s)
                    inline_node.token.children = new_list_siblings
                    if token_replaced_and_retry:
                        continue
                    else:
                        break
        self.tokens = self.node.to_tokens()
        self.node = SyntaxTreeNode(self.tokens)
        return
    def generate_output_md_file(self):
        renderer = MDRenderer()
        output_markdown = renderer.render(self.tokens, options={}, env={})
        output_path = self.get_output_file_path()
        dir_ = dirname(output_path)
        if not path_exists(dir_):
            makedirs(dir_)
        with open(output_path, "w") as f:
            f.write(output_markdown)
        return

class TechTerm:
    def __init__(self, anchor, entry_word, md_file):
        self.anchor = anchor
        self.entry_word = entry_word
        self.md_file = md_file
        return
    def __lt__(self, other):
        if not isinstance(other, TechTerm):
            return NotImplemented
        return len(self.entry_word) < len(other.entry_word)

def commonpath_length(base_path: str, target_path: str) -> int:
    # パスを分割して比較
    common_ = commonpath([base_path, target_path])
    return len(common_)

if __name__ == "__main__": 
    r = Repository(input_dir)
    r.generate(output_dir)
