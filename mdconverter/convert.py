from ipymd import IPythonMD
import sys

arg = ['dummy.ipynb', './', './fig']
_arg = sys.argv

assert len(_arg) >= 2, f'Arguments must be [TARGET, OUTPUT_DIR, FIG_DIR], got {_arg[1:]}'

for idx, i in enumerate(_arg[1:]):
    arg[idx] = i


parser = IPythonMD()
parser.convert_nb(target=arg[0], output_dir=arg[1], fig_dir_name=arg[2])
