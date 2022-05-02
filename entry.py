import os
import time

from lsfiles import ListFiles
import env

from interface import FixEncoding


path: str = f"{env.DOWNLOADS}__TEST__/suite/"
# path: str = f"{env.DOWNLOADS}__TEST__/bad_encoding/"
listFiles: ListFiles = ListFiles("ei")
listFiles.update_extensions({".flac", ".mp3"})
files_list: list[os.DirEntry] = listFiles(path)



# "ëéěȅ"
# fixEncoding = FixEncoding("ëéȩe̋ėêěĕȇe̊ēęèẽe̦ȅ")
# print(fixEncoding.is_invalid())
# print(fixEncoding.fix())



# -> diacritics
# MODIFIERS_RANGE = {
#     "ordinary_diacritics": (0x0300, 0x0333),

#     "overstruck_dicritics": (0x0334, 0x0338),
#     "miscellaneous_additions": (0x0339, 0x033f),
#     "vietnamese_tone_mark": (0x0340, 0x0341),
#     "additions_for_greek": (0x0342, 0x0345),
#     "additions_for_IPA": (0x0346, 0x034a),
#     "IPA_diacritics_for_disordered_speech": (0x034b, 0x034e),
#     "grapheme_joiner": (0x034f, 0x034f),
#     "additions_for_the_uralic_phonetic_alphabet": (0x0350, 0x0357),
#     "miscellaneous_additions": (0x0358, 0x035b),
#     "double_diacritics": (0x035c, 0x0362),
#     "medieval_superscript_letter_diacritics": (0x0363, 0x036f),

#     "german_dialectology": (0x1ab0, 0x1abe),
#     "scots_dialectology": (0x1abf, 0x1aff),

#     "combining_diacritical_marks_for_symbols": (0x20d0, 0x20dc),
#     "enclosing_diacritics": (0x20d8, 0x20dc),
#     "additional_diacritical_mark_for_symbols": (0x20e1, 0x20e1),
#     "additional_enclosing_diacritics": (0x20e2, 0x20e4),
#     "additional_diacritical_marks_for_symbols": (0x20e5, 0x20ff),
# }

# fixEncoding: FixEncoding = FixEncoding("ëéěȅ")
# fixEncoding: FixEncoding = FixEncoding("ëéee̋ėêěĕȇe̊ēęèẽe̦")
# for i in fixEncoding:
#     print(i.encode("utf8"))

cyrillic: set[str] = {chr(0x0300), chr(0x030F), chr(0x0306), chr(0x0321), chr(0x0322), chr(0x0308), chr(0x0304), chr(0x030B), }
latin: set[str] = {chr(i) for i in range(0x0300, 0x036f+1)}

# for f in files_list:
#     fixEncoding = FixEncoding(f.name)
#     if fixEncoding.containsCombining():
#         if fixEncoding.isFixable():
#             fixEncoding.fix()
#         else:
#             r: list[str] = fixEncoding.getNonSubtituable()
#             print(f"cannot fix: {r}")
