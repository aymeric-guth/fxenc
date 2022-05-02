#!/usr/bin/env python3
import re
import raw as ce
import os
import time


import env
import lsfiles  



pattern_dubious_modifiers_ = {
    b"\xe3\x82\x99",
    b"\xe3\x82\x9a",
    # b"\xff\x9f",
    # b"\xff\x9e"
}

def fix_non_standard_accents(s: str, pattern: re.Pattern):
    s_: bytes = s.encode("utf8")
    while (match_oject := pattern.search(s_)):
        offset = match_oject.start()
        key = s_[offset-3:offset+3]
        s_ = s_[:offset-3] + ce.mod_standard_map[key] + s_[offset+3:]
    return s_.decode("utf8")


path = f"{env.DOWNLOADS}__TEST__"
fnc = lsfiles.ListFiles("e")
fnc.update_extensions({".flac", ".mp3"})
files_list = fnc(path)

pattern_dubious_modifiers: bytes = b"|".join(pattern_dubious_modifiers_)
pattern = re.compile(pattern_dubious_modifiers)

start = time.time()
for p in files_list:
    print(p.name)
    if (set(p.name) & ce.modifier_non_standard):
        print(p.name)
        f = fix_non_standard_accents(p.name, pattern)
        print(f)
print(time.time()-start)


def is_ideographic(self):
    if (set(self.str) & ce.global_ideographic):
        return True

    def fix_non_standard_accents(self):
        # s_ = set(self.str)
        # if not(self.str_ & ce.accents_non_standard): return s
        s_ = self.str.encode("utf8")
        while (match_oject := re.search(ce.pattern_dubious_modifiers, s_)):
            offset = match_oject.start()
            key = s_[offset:offset+3]
            s_ = s_[:offset] + ce.accents_standard_map[key] + s_[offset+3:]
        self.str = s_.decode("utf8")
