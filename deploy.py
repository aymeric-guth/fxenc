import os
import shutil
import subprocess

import env

SRC = f"{env.DEV}fix_encoding_dev/"
DST = f"{env.DEV}fix_encoding/"
target_files = [
    "__init__.py",
    "__main__.py",
    "latin.py",
    "japanese.py",
    "merge.py",
    "interface.py",
]

if __name__ == "__main__":
    try:
        os.mkdir(DST)
        os.mkdir(f"{DST}fix_encoding/")
    except FileExistsError:
        shutil.rmtree(DST)
        os.mkdir(DST)
        os.mkdir(f"{DST}fix_encoding/")
    for f in target_files:
        shutil.copy(f"{SRC}{f}", f"{DST}fix_encoding/{f}")
    shutil.copy(f"{SRC}setup.py", f"{DST}setup.py")
    shutil.copy(f"{SRC}README.md", f"{DST}README.md")
    shutil.copy(f"{SRC}LICENSE", f"{DST}LICENSE")
    shutil.copytree(f"{SRC}build_japanese_index/", f"{DST}build_japanese_index/")
    shutil.copytree(f"{SRC}build_latin_index/", f"{DST}build_latin_index/")
    print("Done")