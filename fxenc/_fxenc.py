from .index import STANDARD_MAP_BYTES, STANDARD_MAP_STR, COMBINING_SUPPORTED, COMBINING_FULL, SUPPORTED_RANGE


class FxEnc(object):
    def __init__(self, s: str):
        assert isinstance(s, str)
        self.s: str = s
        self.unique_individual_symbols: set[str] = set(s)
        # NOT_IMPLEMENTED: U+0370 - U+2FA1E
        self.individual_characters: list[str] = [ i for i in self ]
        self.unique_individual_characters: set[str] = { i for i in self }

    def diacritics(self) -> list[str]:
        """returns grapheme(s) with combining diacritics contained in the string passed to __init__"""
        buffer: list[str] = []
        for s in self.individual_characters:
            if (set(s) & COMBINING_FULL):
                buffer.append(s)
        return buffer

    def non_substituable(self) -> list[str]:
        """returns non-substituable grapheme(s)"""
        unique_diacritics: set[str] = self.unique_individual_characters - SUPPORTED_RANGE
        return list(unique_diacritics - STANDARD_MAP_STR.keys())

    def fix(self) -> str:
        """
        verifies the string passed to __init__ contains only substituable grapheme(s)
        substitutes grapheme(s) that uses combining diacritical mark(s) for native version
        """
        unique_diacritics: set[str] = self.unique_individual_characters - SUPPORTED_RANGE
        if(unique_diacritics - STANDARD_MAP_STR.keys()):
            raise NotImplementedError(f"These graphemes ar not substituable (yet):\n{self.non_substituable()}")

        r: list[str] = []
        for s in self.individual_characters:
            r.append(STANDARD_MAP_STR.get(s, s) )
        return "".join(r)

    def __iter__(self):
        self.n: int = 0
        self.max = len(self.s)
        return self

    def __next__(self) -> str:
        """iterates over string according to grapheme(s)"""
        buffer: list[str] = []
        if self.n >= self.max:
            raise StopIteration
        try:
            buffer.append(self.s[self.n])
            while (self.s[self.n+1] in COMBINING_FULL):
                buffer.append(self.s[self.n+1])
                self.n += 1
        except IndexError:
            pass
        finally:
            self.n += 1
            return "".join(buffer)

    def __len__(self):
        """returns number of grapheme(s) in string passed to __init__"""
        return len(self.individual_characters)

    def __bool__(self) -> bool:
        """verifies the string passed to __init__ contains combining diacritical mark(s)"""
        if (self.unique_individual_symbols & COMBINING_SUPPORTED):
            return True
        return False


def quickfix(s: str) -> str:
    try:
        return FxEnc(s).fix()
    except NotImplementedError:
        return s

