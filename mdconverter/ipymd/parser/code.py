import base64
import re
from typing import Dict, Any
import jinja2


def parse_code(meta: Dict[str, Any], template: jinja2.environment.Template, fig_dir_name='fig'):
    lang = meta['language_info']['name']
    style_css = re.compile(r"""<style(".*?"|'.*?'|[^'"])*?>.*?<\/style>""")
    style_inline_css = re.compile(r'style=".*?"')
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def inner(cell: Dict[str, Any]):
        source = cell['source']
        outputs = cell['outputs']
        execution_count = cell['execution_count']
        arg = {
            'lang': lang,
            'source_batch': ''.join(source),
            'stdout_batch': [],
            "stderr_batch": [],
            'error': [],
            'text_plain_batch': [],
            'image_png': [],
            'text_html': []
        }
        counter = 0
        for i in outputs:
            if 'name' in i.keys():
                cont = ''.join(i['text']).replace('<', '&lt;').replace('>', '&gt;')
                arg[f'{i["name"]}_batch'].append(cont)
            elif 'ename' in i.keys():
                tr = '\n'.join(i['traceback']).replace('<', '&lt;').replace('>', '&gt;')
                val = i['evalue'].replace('<', '&lt;').replace('>', '&gt;')
                cont = {'ename': i['ename'], 'evalue': val, 'traceback': ansi_escape.sub('', tr)}
                arg['error'].append(cont)
            elif 'data' in i.keys():
                temp = i['data']
                if 'text/plain' in temp.keys():
                    cont = ''.join(temp['text/plain']).replace('<', '&lt;').replace('>', '&gt;')
                    arg['text_plain_batch'].append(cont)
                if 'image/png' in temp.keys():
                    name = f'{fig_dir_name}/{execution_count}-{counter}.png'
                    with open(name, 'wb') as f:
                        f.write(base64.b64decode(temp['image/png']))
                    counter += 1
                    arg['image_png'].append(name)
                if 'text/html' in temp.keys():
                    html = ''.join(temp['text/html']).replace('\n', '')
                    html = style_css.sub('', html)
                    html = html.replace('class', 'className')
                    while style_inline_css.search(html):
                        i = style_inline_css.search(html)
                        hit = list(filter(lambda x: x!='', html[i.start()+7:i.end()-1].split(';')))
                        inline_css = [tuple(i.split(':')) for i in hit]
                        new_css = ','.join([f'{snake_to_camel(k)}:"{v.strip()}"' for k, v in inline_css])
                        html = list(html)
                        html[i.start():i.end()] = 'style={{' + new_css + '}}'
                        html = ''.join(html)
                    arg['text_html'].append(html)
            else:
                print(f'##### No Hit!! ##### > {i}')
        return template.render(arg)
    return inner


def snake_to_camel(txt: str):
    temp = txt.split('-')
    if len(temp) == 2:
        return temp[0] + temp[1].capitalize()
    return txt
