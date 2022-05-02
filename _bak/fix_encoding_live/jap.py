import re
from functools import partial
"""
UTF-8 implementation for Japanese Language
"""
hiragana_standard_str = [
    "が", "ぎ", "ぐ", 
    "げ", "ご", "ざ", 
    "じ", "ず", "ぜ", 
    "ぞ", "だ", "ぢ", 
    "づ", "で", "ど", 
    "ゔ", "ば", "ぱ", 
    "び", "ぴ", "ぶ", 
    "ぷ", "べ", "ぺ", 
    "ぼ", "ぽ",
]
katakana_standard_str = [
    "ガ", "ギ", "グ",
    "ゲ", "ゴ", "ザ",
    "ジ", "ズ", "ゼ",
    "ゾ", "ダ", "ヂ",
    "ヅ", "デ", "ド",
    "ヷ", "ヸ", "ヹ",
    "ヺ", "バ", "パ",
    "ビ", "ピ", "ブ",
    "プ", "ベ", "ペ",
    "ボ", "ポ", "ヴ",
]
standard_str: list[str] = hiragana_standard_str + katakana_standard_str
standard_bytes: list[bytes] = [ i.encode("utf8") for i in standard_str ]
# hiragana_standard_bytes = [
#     b"\xe3\x81\x8c", b"\xe3\x81\x8e", b"\xe3\x81\x90",
#     b"\xe3\x81\x92",b"\xe3\x81\x94",b"\xe3\x81\x96",
#     b"\xe3\x81\x98",b"\xe3\x81\x9a",b"\xe3\x81\x9c",
#     b"\xe3\x81\x9e",b"\xe3\x81\xa0",b"\xe3\x81\xa2",
#     b"\xe3\x81\xa5",b"\xe3\x81\xa7",b"\xe3\x81\xa9",
#     b"\xe3\x82\x94",b"\xe3\x81\xb0",b"\xe3\x81\xb1",
#     b"\xe3\x81\xb3",b"\xe3\x81\xb4",b"\xe3\x81\xb6",
#     b"\xe3\x81\xb7",b"\xe3\x81\xb9",b"\xe3\x81\xba",
#     b"\xe3\x81\xbc",b"\xe3\x81\xbd",
# ]
# katakana_standard_bytes = [
#     b"\xe3\x82\xac",b"\xe3\x82\xae",b"\xe3\x82\xb0",
#     b"\xe3\x82\xb2",b"\xe3\x82\xb4",b"\xe3\x82\xb6",
#     b"\xe3\x82\xb8",b"\xe3\x82\xba",b"\xe3\x82\xbc",
#     b"\xe3\x82\xbe",b"\xe3\x83\x80",b"\xe3\x83\x82",
#     b"\xe3\x83\x85",b"\xe3\x83\x87",b"\xe3\x83\x89",
#     b"\xe3\x83\xb7",b"\xe3\x83\xb8",b"\xe3\x83\xb9",
#     b"\xe3\x83\xba",b"\xe3\x83\x90",b"\xe3\x83\x91",
#     b"\xe3\x83\x93",b"\xe3\x83\x94",b"\xe3\x83\x96",
#     b"\xe3\x83\x97",b"\xe3\x83\x99",b"\xe3\x83\x9a",
#     b"\xe3\x83\x9c",b"\xe3\x83\x9d",b"\xe3\x83\xb4",
# ]
# standard_bytes: list[bytes] = hiragana_standard_bytes + katakana_standard_bytes
hiragana_non_standard_str = [
    "が", "ぎ", "ぐ",
    "げ", "ご", "ざ",
    "じ", "ず", "ぜ",
    "ぞ", "だ", "ぢ",
    "づ", "で", "ど",
    "ゔ", "ば", "ぱ",
    "び", "ぴ", "ぶ",
    "ぷ", "べ", "ぺ",
    "ぼ", "ぽ",
]
katakana_non_standard_str = [
    "ガ", "ギ", "グ",
    "ゲ", "ゴ", "ザ",
    "ジ", "ズ", "ゼ",
    "ゾ", "ダ", "ヂ",
    "ヅ", "デ", "ド",
    "ヷ", "ヸ", "ヹ",
    "ヺ", "バ", "パ",
    "ビ", "ピ", "ブ",
    "プ", "ベ", "ペ",
    "ボ", "ポ", "ヴ",
]
non_standard_str: list[str] = hiragana_non_standard_str + katakana_non_standard_str
non_standard_bytes: list[bytes] = [ i.encode("utf8") for i in non_standard_str ]
# hiragana_non_standard_bytes = [
#     b'\xe3\x81\x8b\xe3\x82\x99', b'\xe3\x81\x8d\xe3\x82\x99', b'\xe3\x81\x8f\xe3\x82\x99',
#     b'\xe3\x81\x91\xe3\x82\x99', b'\xe3\x81\x93\xe3\x82\x99', b'\xe3\x81\x95\xe3\x82\x99',
#     b'\xe3\x81\x97\xe3\x82\x99', b'\xe3\x81\x99\xe3\x82\x99', b'\xe3\x81\x9b\xe3\x82\x99',
#     b'\xe3\x81\x9d\xe3\x82\x99', b'\xe3\x81\x9f\xe3\x82\x99', b'\xe3\x81\xa1\xe3\x82\x99',
#     b'\xe3\x81\xa4\xe3\x82\x99', b'\xe3\x81\xa6\xe3\x82\x99', b'\xe3\x81\xa8\xe3\x82\x99',
#     b'\xe3\x81\x86\xe3\x82\x99', b'\xe3\x81\xaf\xe3\x82\x99', b'\xe3\x81\xaf\xe3\x82\x9a',
#     b'\xe3\x81\xb2\xe3\x82\x99', b'\xe3\x81\xb2\xe3\x82\x9a', b'\xe3\x81\xb5\xe3\x82\x99',
#     b'\xe3\x81\xb5\xe3\x82\x9a', b'\xe3\x81\xb8\xe3\x82\x99', b'\xe3\x81\xb8\xe3\x82\x9a',
#     b'\xe3\x81\xbb\xe3\x82\x99', b'\xe3\x81\xbb\xe3\x82\x9a',
# ]
# katakana_non_standard_bytes = [
#     b'\xe3\x82\xab\xe3\x82\x99', b'\xe3\x82\xad\xe3\x82\x99', b'\xe3\x82\xaf\xe3\x82\x99',
#     b'\xe3\x82\xb1\xe3\x82\x99', b'\xe3\x82\xb3\xe3\x82\x99', b'\xe3\x82\xb5\xe3\x82\x99',
#     b'\xe3\x82\xb7\xe3\x82\x99', b'\xe3\x82\xb9\xe3\x82\x99', b'\xe3\x82\xbb\xe3\x82\x99',
#     b'\xe3\x82\xbd\xe3\x82\x99', b'\xe3\x82\xbf\xe3\x82\x99', b'\xe3\x83\x81\xe3\x82\x99',
#     b'\xe3\x83\x84\xe3\x82\x99', b'\xe3\x83\x86\xe3\x82\x99', b'\xe3\x83\x88\xe3\x82\x99',
#     b'\xe3\x83\xaf\xe3\x82\x99', b'\xe3\x83\xb0\xe3\x82\x99', b'\xe3\x83\xb1\xe3\x82\x99',
#     b'\xe3\x83\xb2\xe3\x82\x99', b'\xe3\x83\x8f\xe3\x82\x99', b'\xe3\x83\x8f\xe3\x82\x9a',
#     b'\xe3\x83\x92\xe3\x82\x99', b'\xe3\x83\x92\xe3\x82\x9a', b'\xe3\x83\x95\xe3\x82\x99',
#     b'\xe3\x83\x95\xe3\x82\x9a', b'\xe3\x83\x98\xe3\x82\x99', b'\xe3\x83\x98\xe3\x82\x9a',
#     b'\xe3\x83\x9b\xe3\x82\x99', b'\xe3\x83\x9b\xe3\x82\x9a', b'\xe3\x82\xa6\xe3\x82\x99',
# ]
# non_standard_bytes: list[bytes] = hiragana_non_standard_bytes + katakana_non_standard_bytes
standard_map: dict[bytes, bytes] = dict(zip(
    non_standard_bytes, standard_bytes
))
modifiers: set[str] = {"゙", "゚", }
p: list[bytes] = [i.encode("utf8") for i in modifiers]
pattern = re.compile( b"|".join(p) )

def fix_(pattern: re.Pattern, standard_map: dict[bytes, bytes], s: str) -> str:
    offset: int
    key: bytes
    s_: bytes = s.encode("utf8")
    while (match_oject := pattern.search(s_)):
        offset = match_oject.start()
        key = s_[offset-3:offset+3]
        s_ = s_[:offset-3] + standard_map[key] + s_[offset+3:]
    return s_.decode("utf8")

fix = partial(fix_, pattern=pattern, standard_map=standard_map)

def is_invalid_(modifiers: set[str], s: str) -> bool:
    if (set(s) & modifiers):
        return True
    return False

is_invalid = partial(is_invalid_, modifiers=modifiers)
