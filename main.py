#!/usr/bin/env python
from logging import getLogger
from os import makedirs as makedirs
from os.path import abspath as abspath
from os.path import dirname as dirname
from os.path import exists as path_exists
from os.path import join as path_join
from os.path import relpath as relpath
from posixpath import abspath
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
    def __init__(self, input_dir, output_dir):
        import glob
        pathname = path_join(input_dir, '**', '*.md')
        md_file_paths = glob.glob(pathname, recursive=True)
        self.md_files = [MarkDownFile(f) for f in md_file_paths]
        logger.info("Markdown files, which this script found, are:")
        for f in md_file_paths:
            logger.info(" - " + f)
        self.input_dir = input_dir    
        self.output_dir = output_dir    
        return
    def generate(self, output_dir='output'):
        if not path_exists(output_dir):
            makedirs(output_dir)
        else:
            logger.warning("Directory {} is already exist.".format(output_dir))
        [ f.generate_anchor() for f in self.md_files]
        # [NOTE]: 全markdown fileの全Tech Termを文字列長降順でソートしてループする
        all_tech_terms = [ t for f in self.md_files for t in f.tech_terms]
        for t in sorted(all_tech_terms, reverse=True):
            [ f.generate_link(t) for f in self.md_files]
        input_dir = self.input_dir
        output_dir = self.output_dir
        [ f.generate_output_md_file(input_dir, output_dir) for f in self.md_files]
        return

import re
re_url = re.compile(r'<!-- 記事URL:(.*) -->')
re_term = re.compile(r'(#+) (.*) <!-- entry_word_and_anchor:(\w*) -->')
re_gen_achor = re.compile(r'<!-- entry_word_and_anchor:(\w*) -->')
class MarkDownFile:
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as f:
            self.text = f.read()
        # [NOTE]: 記事URL(=https:~ ) の部分だけ後方参照して取り出す
        ret = re.findall(re_url, self.text)
        if len(ret) != 1:
            logger.fatal('Markdown File {} should have only one url.'.format(path))
            logger.fatal([str(ret) for ret in ret])
            self.url = None
        else:
            self.url = ret[0]
            logger.debug(ret[0])
        # [NOTE]: TechTermのentry_wordとanchorを取得
        ret = re.findall(re_term, self.text)
        tech_terms = []
        for tech_term_and_anchor in ret:
            entry_words = tech_term_and_anchor[1]
            anchor = tech_term_and_anchor[2]
            logger.debug(anchor)
            logger.debug(entry_words)
            for entry_word in [ i.strip() for i in entry_words.split('|')]:
                t = TechTerm(anchor, entry_word, self)
                tech_terms.append(t)
        self.tech_terms = tech_terms
        return
    def generate_anchor(self):
        term_with_achor = r'<a id="\3"></a>\n'
        term_with_achor += r'\1 \2 '
        term_with_achor += r'<!-- entry_word_and_anchor:\3 -->'
        self.text = re.sub(re_term, 
                           term_with_achor,
                           self.text)
        return
    def generate_link(self, tech_term):
        entry_word = tech_term.entry_word
        entry_word_with_link = r'\1'
        entry_word_with_link += r'<a href="' + tech_term.md_file.url
        entry_word_with_link += tech_term.anchor
        entry_word_with_link += r'"> ' + tech_term.entry_word
        entry_word_with_link += r' </a>'

        pattern = r'^(?!#)(.*){0}(?!(?!.*<a).*<\/a>)(?!(?!.*<!--).*-->)'.format(entry_word)
        re_sub = re.compile(pattern)
        logger.debug(pattern)
        logger.debug(re.search(pattern, self.text, flags=re.MULTILINE))
        self.text = re.sub(pattern, entry_word_with_link, self.text, flags=re.MULTILINE)

        return
    def generate_output_md_file(self, input_dir, output_dir):
        output_path = self._replase_base_dir(self.path, input_dir, output_dir)
        dir_ = dirname(output_path)
        if not path_exists(dir_):
            makedirs(dir_)
        with open(output_path, "w") as f:
            f.write(self.text)
        return
    def _replase_base_dir (self, target_path, old_base, new_base):
        relative_path = relpath(target_path, old_base)
        return path_join(new_base, relative_path)

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
if __name__ == "__main__": 
    r = Repository(input_dir, output_dir)
    r.generate()
