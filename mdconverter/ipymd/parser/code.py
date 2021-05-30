import base64
import re
from typing import Any, Callable, Dict
import jinja2


def parse_code(
    meta: Dict[str, Any],
    template: jinja2.environment.Template,
    output_dir='./',
    fig_dir_name='fig'
) -> Callable[Dict[str, Any], str]:

    lang = meta['language_info']['name']
    style_css = re.compile(r"""<style(".*?"|'.*?'|[^'"])*?>.*?<\/style>""")
    style_inline_css = re.compile(r'style=".*?"')
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def inner(cell: Dict[str, Any]):
        source = cell['source']
        outputs = cell['outputs']
        execution_count = cell['execution_count']
        arg = {
            'error': [],
            'image_png': [],
            'text_html': [],
            'text_plain_batch': [],
            'stdout_batch': [],
            "stderr_batch": [],
        }
        counter = 0
        for i in outputs:
            if 'name' in i.keys():
                cont = ''.join(i['text'])
                arg[f'{i["name"]}_batch'].append(cont)
            elif 'ename' in i.keys():
                tr = '\n'.join(i['traceback'])
                val = html_escape(i['evalue'])
                cont = {'ename': i['ename'], 'evalue': val, 'traceback': ansi_escape.sub('', tr)}
                arg['error'].append(cont)
            elif 'data' in i.keys():
                temp = i['data']
                if 'text/plain' in temp.keys():
                    cont = ''.join(temp['text/plain'])
                    arg['text_plain_batch'].append(cont)
                if 'image/png' in temp.keys():
                    name = f'{fig_dir_name}/{execution_count}-{counter}.png'
                    path = f'{output_dir}/{name}'
                    with open(path, 'wb') as f:
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
        fe = ''
        for k, v in arg.items():
            if len(v) != 0:
                fe = k
                break
        return template.render({
            'lang': lang,
            'source_batch': ''.join(source),
            'output': arg if sum([len(i) for i in arg.values()]) != 0 else {},
            'first_element': fe
        })
    return inner


def snake_to_camel(txt: str):
    temp = txt.split('-')
    if len(temp) == 2:
        return temp[0] + temp[1].capitalize()
    return txt


def html_escape(txt: str):
    exp = {
        '<': '&lt;',
        '>': '&gt;',
        '{': '&#123;',
        '}': '&#125;',
    }
    for k, v in exp.items():
        txt = txt.replace(k, v)
    return txt
