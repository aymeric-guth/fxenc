import pathlib
import subprocess
import os
import shutil


implemented_indexes = [
    'japanese',
    'latin'
]

root = pathlib.PurePath(__file__).parent
fxenc = root.parent / 'fxenc'
# shutil.rmtree(fxenc / 'index')
os.makedirs(fxenc / 'index')


STANDARD_MAP_BYTES_TOKEN = []
STANDARD_MAP_STR_TOKEN = []
COMBINING_SUPPORTED_TOKEN = []
COMBINING_SUPPORTED_TOKEN = []
COMBINING_FULL_TOKEN = []
SUPPORTED_RANGE_TOKEN = []
STANDARD_MAP_BYTES_TEMPLATE = 'STANDARD_MAP_BYTES: dict[bytes, bytes] = {}\n'
STANDARD_MAP_STR_TEMPLATE = 'STANDARD_MAP_STR: dict[str, str] = {}\n'
COMBINING_SUPPORTED_TEMPLATE = 'COMBINING_SUPPORTED: set[str] = {}\n'
COMBINING_FULL_TEMPLATE = 'COMBINING_FULL: set[str] = {}\n'
SUPPORTED_RANGE_TEMPLATE = 'SUPPORTED_RANGE: set[str] = {}\n'
IMPORT_TEMPLATE = 'from . import {}\n'


for idx in implemented_indexes:
    index_builder = str(root / f'index_{idx}' / 'build_index.py')
    os.chmod(index_builder, 0o755)
    subprocess.run(['sh', '-c', index_builder])
    shutil.move(str(root / f'{idx}.py'), str(fxenc / 'index' / f'{idx}.py'))
    STANDARD_MAP_BYTES_TOKEN.append(f'{idx}.STANDARD_MAP_BYTES')
    STANDARD_MAP_STR_TOKEN.append(f'{idx}.STANDARD_MAP_STR')
    COMBINING_SUPPORTED_TOKEN.append(f'{idx}.COMBINING_SUPPORTED')
    COMBINING_FULL_TOKEN.append(f'{idx}.COMBINING_FULL')
    SUPPORTED_RANGE_TOKEN.append(f'{idx}.SUPPORTED_RANGE')
    with open(fxenc / 'index' / '__init__.py', 'a') as f:
        f.write(IMPORT_TEMPLATE.format(idx))

with open(fxenc / 'index' / '__init__.py', 'a') as f:
    f.write('\n\n')
    f.write(STANDARD_MAP_BYTES_TEMPLATE.format(' | '.join(STANDARD_MAP_BYTES_TOKEN)))
    f.write(STANDARD_MAP_STR_TEMPLATE.format(' | '.join(STANDARD_MAP_STR_TOKEN)))
    f.write(COMBINING_SUPPORTED_TEMPLATE.format(' | '.join(COMBINING_SUPPORTED_TOKEN)))
    f.write(COMBINING_FULL_TEMPLATE.format(' | '.join(COMBINING_FULL_TOKEN)))
    f.write(SUPPORTED_RANGE_TEMPLATE.format(' | '.join(SUPPORTED_RANGE_TOKEN)))
