from typing import Any

from parse_combining import main as pc
from parse_raw import main as pr
from template import lookup_table

"""
Valid for LATIN charset (U+0000 - U+02AF)
    are excluded characters using more than 1 diacritical mark
    due to lack of use in latin languages

Aggregate module for building the actual useful data:
    standard_str: list[str]
    standard_bytes: list[bytes]
    non_standard_str: list[str]
    non_standard_bytes: list[bytes]
    standard_map: dict[bytes, bytes]

The idea is to match special combining characters using '''modifiers: set[str]'''
then substituing to native version of the diacriticaly marked character 
using '''standard_map: dict[bytes, bytes]'''
"""

combining: list[tuple[Any, ...]] = []
native: list[tuple[Any, ...]] = []
combining = pc()
native = pr()
# modifiers_str: list[str] = []
# modifiers: set[str] = set(modifiers_str)
# modifiers: set[str] = {i.decode("utf8") for i in modifiers_bytes}


lookup_table_combining: dict[str, str] = { k: v for (v, k) in combining }
modifiers: set[str] = {
    lookup_table_combining[i] for i in 
    { m[2] for m in native }
}
# p: list[bytes] = [i.encode("utf8") for i in modifiers]
# pattern: re.Pattern = re.compile(b"|".join(p))
# modifiers_: set[str] = set(lookup_table_combining.values())

standard_str: list[str] = []
standard_bytes: list[bytes] = []
non_standard_str: list[str] = []
non_standard_bytes: list[bytes] = []

l: str
mod: str
out_ns: str
for case, letter, modifier, out in native:
    l = lookup_table["LATIN"][case][letter]
    mod = lookup_table_combining[modifier]
    out_ns = l + mod
    standard_str.append(out)
    standard_bytes.append(out.encode("utf8"))
    non_standard_str.append(out_ns)
    non_standard_bytes.append(out_ns.encode("utf8"))

standard_map: dict[bytes, bytes] = dict(zip(
    non_standard_bytes, standard_bytes,
))
UNICODE_LOWER_RANGE: int = 0x0020
UNICODE_UPPER_RANGE: int = 0x036f
SUPPORTED_RANGE: list[str] = [
    chr(i)
    for i in range(UNICODE_LOWER_RANGE, UNICODE_UPPER_RANGE)
    if chr(i)
]

with open("latin.py", "w") as file:
    file.write("### GENERATED AUTOMATICALLY ###\n")
    file.write("import re\n\n")
    # for debug purposes and eventual future use
    # file.write("STANDARD_STR: list[str] = [\n")
    # for i in standard_str:
    #     file.write(f'\t"{i}",\n')
    # file.write("]\n")
    # file.write("STANDARD_BYTES: list[bytes] = [\n")
    # for i in standard_bytes:
    #     file.write(f'\t{i},\n')
    # file.write("]\n")
    # file.write("NON_STANDARD_STR: list[str] = [\n")
    # for i in non_standard_str:
    #     file.write(f'\t"{i}",\n')
    # file.write("]\n")
    # file.write("NON_STANDARD_BYTES: list[bytes] = [\n")
    # for i in non_standard_bytes:
    #     file.write(f'\t{i},\n')
    # file.write("]\n")
    file.write("STANDARD_MAP: dict[bytes, bytes] = {\n")
    for k, v in standard_map.items():
        file.write(f"\t{k}: {v},\n")
    file.write("}\n")
    file.write("MODIFIERS: set[str] = {\n")
    for i in modifiers:
        file.write(f'\t"{i}",\n')
    file.write("}\n")
    file.write('p: list[bytes] = [i.encode("utf8") for i in MODIFIERS]\n')
    file.write('PATTERN: re.Pattern = re.compile(b"|".join(p))\n')
    file.write("SUPPORTED_RANGE: set[str] = {\n")
    for i in SUPPORTED_RANGE:
        # for debug purposes
        # if i == '"':
        #     file.write(f"\t'{hex(ord(i))}: {i}',\n")
        # elif i == "\\":
        #     file.write(f"\t'{hex(ord(i))}: \{i}',\n")
        # else:
        #     file.write(f'\t"{hex(ord(i))}: {i}",\n')
        if i == '"':
            file.write(f"\t'{i}',\n")
        elif i == "\\":
            file.write(f"\t'\{i}',\n")
        else:
            file.write(f'\t"{i}",\n')
    file.write("}\n")
