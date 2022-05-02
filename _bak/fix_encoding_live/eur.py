import re
from functools import partial
"""
UTF-8 implementation for european languages (French, German, Italian, Spanish, Portugese, Polish, Czech, Serbian)
"""
standard_str = (
    'À', 'Á', 'Â', 'Ä', 'Ã', 'Å', 'Ą',
    'à', 'á', 'â', 'ä', 'ã', 'å', 'ą',
    'Ć', 'Ĉ', 'Ç',
    'ć', 'ĉ', 'ç',
    'È', 'É', 'Ê', 'Ë', 'Ę',
    'è', 'é', 'ê', 'ë', 'ę',
    'Ğ',
    'ğ',
    'Ì', 'Í', 'Î', 'Ï',
    'ì', 'í', 'î', 'ï',
    # 'Ł', 
    # 'ł',
    'Ǹ', 'Ń', 'Ñ', 'Ņ', 'Ň',
    'ǹ', 'ń', 'ñ', 'ņ', 'ň',
    'Ò', 'Ó', 'Ô', 'Ö', 'Õ',
    'ò', 'ó', 'ô', 'ö', 'õ',
    'Ś', 'Ş',
    'ś', 'ş',
    'Ù', 'Ú', 'Û', 'Ü',
    'ù', 'ú', 'û', 'ü',
    'Ý', 'Ŷ', 'Ÿ',
    'ý', 'ŷ', 'ÿ',
    'Ź', 'Ż',
    'ź', 'ż',
)
standard_bytes = [ i.encode("utf8") for i in standard_str ]
non_standard_str = (
    'À', 'Á', 'Â', 'Ä', 'Ã', 'Å', 'Ą', 
    'à', 'á', 'â', 'ä', 'ã', 'å', 'ą',
    'Ć', 'Ĉ', 'Ç',
    'ć', 'ĉ', 'ç',
    'È', 'É', 'Ê', 'Ë', 'Ę',
    'è', 'é', 'ê', 'ë', 'ę',
    'Ğ', 
    'ğ',
    'Ì', 'Í', 'Î', 'Ï',
    'ì', 'í', 'î', 'ï',
    'Ǹ', 'Ń', 'Ñ', 'Ņ', 'Ň',
    'ǹ', 'ń', 'ñ', 'ņ', 'ň',
    'Ò', 'Ó', 'Ô', 'Ö', 'Õ',
    'ò', 'ó', 'ô', 'ö', 'õ',
    'Ś', 'Ş',
    'ś', 'ş',
    'Ù', 'Ú', 'Û', 'Ü',
    'ù', 'ú', 'û', 'ü',
    'Ý', 'Ŷ', 'Ÿ',
    'ý', 'ŷ', 'ÿ',
    'Ź', 'Ż',
    'ź', 'ż',
)
non_standard_bytes: list[bytes] = [ i.encode("utf8") for i in non_standard_str ]
standard_map: dict[bytes, bytes] = dict(zip(
    non_standard_bytes, standard_bytes,
))

modifiers_bytes: list[bytes] = []
for n in range(0x0300, 0x0361):
    modifiers_bytes.append(chr(n).encode("utf8"))
for n in range(0x1DC0, 0x1F00):
    modifiers_bytes.append(chr(n).encode("utf8"))
print(len(modifiers_bytes))
# modifiers_str: list[str] = [ i.decode("utf8") for i in modifiers_bytes ]
# modifiers: set[str] = set(modifiers_str)
modifiers: set[str] = { i.decode("utf8") for i in modifiers_bytes }
# p: list[bytes] = [ i.encode("utf8") for i in modifiers ]
pattern: re.Pattern = re.compile(b"|".join(modifiers_bytes))

def fix_(pattern: re.Pattern, standard_map: dict[bytes, bytes], s: str) -> str:
    offset: int
    key: bytes
    s_: bytes = s.encode("utf8")

    cyrillic = {chr(i) for i in range(0x0400, 0x0600)}
    if (set(s) & cyrillic):
        # print(s)
        # print("Cyrillic")
        return
    try:
        while ( match_oject := pattern.search(s_) ):
            offset = match_oject.start()
            key = s_[offset-1:offset+2]
            s_ = s_[:offset-1] + standard_map[key] + s_[offset+2:]
    except:
        print("Exception")
        print(s)
        print(s_[offset-1:])
        # print(offset)
        # with open("log.txt", "a") as f:
        #     f.write(f"{s=}\n")
        #     f.write(f"{offset=}\n")
        #     f.write(f"{key=}\n")
        #     f.write(f"{s_=}\n\n")
    return s_.decode("utf8")


# fix = lambda self, x: fix_(pattern=pattern, standard_map=standard_map, s=x)
fix = lambda x: fix_(pattern=pattern, standard_map=standard_map, s=x)
# fix = partial(fix_, pattern=pattern, standard_map=standard_map)

def is_invalid_(modifiers: set[str], s: str) -> bool:
    if ( set(s) & modifiers ):
        return True
    return False

# is_invalid = lambda self, x: is_invalid_(modifiers=modifiers, s=x)
is_invalid = lambda x: is_invalid_(modifiers=modifiers, s=x)
# is_invalid = partial(is_invalid_, modifiers=modifiers)

# b: bytes = b"S\xcc\xa7"
# s: str = 'ş'
# print(b.decode("utf8"))
# print(s.encode("utf8"))

