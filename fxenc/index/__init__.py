from . import japanese
from . import latin


STANDARD_MAP_BYTES: dict[bytes, bytes] = japanese.STANDARD_MAP_BYTES | latin.STANDARD_MAP_BYTES
STANDARD_MAP_STR: dict[str, str] = japanese.STANDARD_MAP_STR | latin.STANDARD_MAP_STR
COMBINING_SUPPORTED: set[str] = japanese.COMBINING_SUPPORTED | latin.COMBINING_SUPPORTED
COMBINING_FULL: set[str] = japanese.COMBINING_FULL | latin.COMBINING_FULL
SUPPORTED_RANGE: set[str] = japanese.SUPPORTED_RANGE | latin.SUPPORTED_RANGE
