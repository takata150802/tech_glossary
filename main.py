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
        print(md_file_paths)
        return
    def generate(self, output_dir='output'):
        import os
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        else:
            logger.warning("Directory {} is already exist.".format(output_dir))
        [ f.generate_anchor() for f in self.md_files]
        [ f.generate_output_md_file(output_dir) for f in self.md_files]
        return

import re
re_url = re.compile(r'<!--- 記事URL:(.*) --->')
re_term = re.compile(r'#+ (.*) <!--- entry_word_and_anchor:(\w*) --->')
re_gen_achor = re.compile(r'<!--- entry_word_and_anchor:(\w*) --->')
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
            entry_words = tech_term_and_anchor[0]
            anchor = tech_term_and_anchor[1]
            entry_words = [ i.strip() for i in entry_words.split('|')]
            logger.debug(anchor)
            logger.debug(entry_words)
            t = TechTerm(anchor, entry_words)
            tech_terms.append(t)
        self.tech_terms = tech_terms
        return
    def generate_anchor(self):
        self.text = re.sub(re_gen_achor, 
                           r'<!--- entry_word_and_anchor:\1 ---><a id="\1"></a>',
                           self.text)
        return
    def generate_output_md_file(self, output_dir):
        output_path = output_dir + '/' + self.path
        with open(output_path, "w") as f:
            f.write(self.text)
        return

class TechTerm:
    def __init__(self, anchor, entry_words):
        self.anchor = anchor
        self.headwords = entry_words
        return

if __name__ == "__main__": 
    r = Repository()
    r.generate()
