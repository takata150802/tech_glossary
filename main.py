#!/usr/bin/env python
import argparse
import logging
from logging import getLogger
parser = argparse.ArgumentParser(description='Set logging level')
parser.add_argument('--log-level', dest='log_level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    default='WARNING', help='Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
args = parser.parse_args()
logger = getLogger(__name__)
numeric_level = getattr(logging, args.log_level, None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.log_level)
logging.basicConfig(level=numeric_level)

class Repository:
    def __init__(self):
        import glob
        md_file_paths = glob.glob('*.md')
        self.md_files = [MarkDownFile(f) for f in md_file_paths]
        logger.info("Markdown files, which this script found, are:")
        for f in md_file_paths:
            logger.info(" - " + f)
        return
    def generate(self, output_dir='output'):
        import os
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        else:
            logger.warning("Directory {} is already exist.".format(output_dir))
        [ f.generate_anchor() for f in self.md_files]
        # [NOTE]: 全markdown fileの全Tech Termを文字列長降順でソートしてループする
        all_tech_terms = [ t for f in self.md_files for t in f.tech_terms]
        for t in sorted(all_tech_terms, reverse=True):
            [ f.generate_link(t) for f in self.md_files]
        [ f.generate_output_md_file(output_dir) for f in self.md_files]
        return

import re
re_url = re.compile(r'<!-- 記事URL:(.*) -->')
re_term = re.compile(r'(#+) (.*) <!-- entry_word_and_anchor:(\w*) -->')
re_gen_achor = re.compile(r'<!-- entry_word_and_anchor:(\w*) -->')
class MarkDownFile:
    def __init__(self,path):
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
        entry_word_with_link += r'#' + tech_term.anchor
        entry_word_with_link += r'"> ' + tech_term.entry_word
        entry_word_with_link += r' </a>'

        pattern = r'^(?!#)(.*){0}(?!(?!.*<a).*<\/a>)(?!(?!.*<!--).*-->)'.format(entry_word)
        re_sub = re.compile(pattern)
        logger.debug(pattern)
        logger.debug(re.search(pattern, self.text, flags=re.MULTILINE))
        self.text = re.sub(pattern, entry_word_with_link, self.text, flags=re.MULTILINE)

        return
    def generate_output_md_file(self, output_dir):
        output_path = output_dir + '/' + self.path
        with open(output_path, "w") as f:
            f.write(self.text)
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
if __name__ == "__main__": 
    r = Repository()
    r.generate()
