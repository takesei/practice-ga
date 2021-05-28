import glob
import json
import os

from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader
from .parser import parse_code, parse_md, parse_raw



class IPythonMD():
    def __init__(self, template: str = ''):
        template = template if template != '' else f'{os.path.dirname(__file__)}/jinja'
        self.jinjaenv = Environment(loader=FileSystemLoader(template, encoding='utf8'))        
        self.template = {
            'code'    : self.jinjaenv.get_template('cell-code.md'),
            'markdown': self.jinjaenv.get_template('cell-md.md'),
            'raw'     : self.jinjaenv.get_template('cell-raw.md'),
            'report'  : self.jinjaenv.get_template('report.md')
        }

        self.parsers = {
            'code'    : parse_code({'language_info': {'name': ''}}, self.template['code']),
            'markdown': parse_md({}, self.template['markdown']),
            'raw'     : parse_raw({}, self.template['raw'])
        }

    def parse_cell(self, cell: Dict[str, Any]):
        ctype = cell['cell_type']
        return self.parsers[ctype](cell)

    def convert_nb(self, target: str, output_dir: str='.', fig_dir_name: str='fig'):
        with open(target, 'r') as f:
            nb = json.load(f)

        self.parsers = {
            'code'    : parse_code(nb['metadata'], self.template['code'], fig_dir_name),
            'markdown': parse_md(nb['metadata'], self.template['markdown']),
            'raw'     : parse_raw(nb['metadata'], self.template['raw'])
        }

        os.makedirs(fig_dir_name, exist_ok=True)

        temp = '\n'.join([self.parse_cell(i) for i in nb['cells']])
        with open(f'{output_dir}/{os.path.basename(target).split(".")[0]}.md', 'w') as f:
            f.write(self.template['report'].render({'content': temp}))
