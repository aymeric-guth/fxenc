start = time.time()
total = 0
for _ in range(1):
    for p in files_list:
        # r = [ i.encode("utf8") for i in p.name ]
        # print(re.search(pattern_dubious_modifiers, p.name.encode("utf8")))
        if (set(p.name) & ce.modifier_non_standard):
            f = fix_non_standard_accents(p.name)
            # print(f)
            # print(p.name)
for _ in range(1):
    for p in files_list:
        # r = [ i.encode("utf8") for i in p.name ]
        # print(re.search(pattern_dubious_modifiers, p.name.encode("utf8")))
        if (set(p.name) & ce.modifier_non_standard):
            f = fix_non_standard_accents_(p.name)
print(time.time()-start)
re.finditer


# for path, file_name, ext in files_list:
#     f = fix_non_standard_accents(file_name)
#     os.rename(f"{path}{file_name}{ext}", f"{path}{f}{ext}")
