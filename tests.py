from random import choices, choice

from interface import FixEncoding


fixEncoding = FixEncoding("a")
chars = list(fixEncoding.STANDARD_MAP_STR.keys())
chars.extend([chr(i) for i in range(0x0041, 0x005A)])
chars.extend([chr(i) for i in range(0x0061, 0x007A)])

test_values = []
for _ in range(100):
    test_values.append(
        "".join(choices(chars, k=choice(range(1, 20))))
    )

for i in test_values:
    print(i)
    fixEncoding = FixEncoding(i)
    if fixEncoding.containsCombining():
        if fixEncoding.isFixable():
            pass
        else:
            raise ValueError
    else:
        print(i)
        raise ValueError
