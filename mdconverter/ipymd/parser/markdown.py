from typing import Dict, Any
import jinja2

def parse_md(meta: Dict[str, Any], template:jinja2.environment.Template):
    def inner(cell: Dict[str, Any]):
        source = cell['source']
        return template.render({'source_batch': ''.join(source)})
    return inner