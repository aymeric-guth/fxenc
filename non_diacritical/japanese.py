#!/usr/bin/env python3
import os
import re
from collections import defaultdict

import env

count = 0
lines = []
# with open(f"{env.DOWNLOADS}ヒデとロザンナ - しんぐるこれくしょん.cue", "rb") as f:
#     raw_data = f.read()
#     data = raw_data.split(b"\r\n")
#     result = []
#     for i in data:
#         try:
#             result.append(i.decode("utf8"))
#         except UnicodeDecodeError:
#             pattern = br"^(\s{4}(TITLE|PERFORMER|FILE)\s)\"(.*)(?=\")\"$"
#             match_object = re.search(pattern, i)
#             if match_object is None:
#                 pattern = br"^((TITLE|PERFORMER|FILE)\s)\"(.*)(?=\")\"(.*)$"
#                 match_object = re.search(pattern, i)
#                 entry = (
#                     match_object.group(1),
#                     match_object.group(3), 
#                     match_object.group(4),
#                     b"\n"
#                 )
#                 lines.append(entry)
#             else:
#                 entry = (
#                     match_object.group(1),
#                     match_object.group(3), 
#                     b"", 
#                     b"\n"
#                 )
#                 lines.append(entry)
#                 # print(match_object.group(2))

#     print(count)
miss = 0
hit = 0


def assert_encoding(data: bytes) -> str:
    for e in encodings:
        try:
            data.decode(e)
            return e
        except UnicodeDecodeError as err:
            print(err)
            continue
    else:
        return "not found"    

# result = []
# for i in data:
#     r = assert_encoding(i)
#     result.append(i.decode(r))


# with open("test.cue", "wb") as file:
#     s = "\n".join(result)
#     file.write(s.encode("utf8"))


encodings = (
    # "cp932",
    # "euc_jp",
    # "euc_jis_2004",
    # "euc_jisx0213",
    # "iso2022_jp",
    # "iso2022_jp_1",
    # "iso2022_jp_2",
    # "iso2022_jp_2004",
    # "iso2022_jp_3",
    # "iso2022_jp_ext",
    # "shift_jis",
    # "shift_jis_2004",
    "shift_jisx0213",
)

with open(f"{env.DOWNLOADS}ヒデとロザンナ - しんぐるこれくしょん.cue", "rb") as f:
    data = f.read().split(b"\r\n")

titles = [ i for i in data[6:-1:6][1:] ]
results = defaultdict(int)
even = 0
odd = 0
for i in titles:
    print(i[11:-1])

r = [(results[i], i) for i in results]
r.sort(reverse=True)
# for i in r:
#     print(i)
results: dict[str, int] = {}
for e in encodings:
    total: int = 0
    hit: int = 0
    miss: int = 0
    d = b'\xe7\xb2\x8b\xaa\x86\xe3\x82\x8f\x95'
    # for d in titles:
        
    try:
        # d[11:-1].decode(e)
        d.decode(e)
        hit += 1
        # print(d[11:-1].decode(e))
        # print(e, d.decode(e))
    except UnicodeDecodeError as err:
        miss += 1
        # print(d)
        # print(err)
        # continue
    finally:
        total += 1
    # print()
    results[e] = {"hit": hit, "miss": miss, "total": total}

for i in results:
    print(i, results[i])

# (88, '0xe3')
# (64, '0x81')
# (24, '0x82')
# (17, '0xe6')
# (13, '0xae')
# (12, '0x83')



