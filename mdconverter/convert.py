import glob
import os
import sys

from ipymd import IPythonMD

arg = ['dummy.ipynb', './', './fig']
_arg = sys.argv

assert len(_arg) >= 2, f'Arguments must be [TARGET, OUTPUT_DIR, FIG_DIR_NAME], got {_arg[1:]}'

for idx, i in enumerate(_arg[1:]):
    arg[idx] = i

assert os.path.exists(arg[0]), f'Target file not found, got {arg[0]}'

target = [arg[0]] if os.path.isfile(arg[0]) else glob.glob(f'{arg[0]}/**/*.ipynb', recursive=True)

parser = IPythonMD()

for f in target:
    print(f"""
        target={f},
        output_dir='{arg[1]}/{os.path.dirname(f)[len(arg[0]) + 1:]}',
        fig_dir_name={arg[2]}
    """)

    parser.convert_nb(
        target=f,
        output_dir=f'{arg[1]}/{os.path.dirname(f)[len(arg[0]) + 1:]}',
        fig_dir_name=arg[2]
    )
