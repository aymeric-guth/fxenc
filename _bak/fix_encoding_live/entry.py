from lsfiles import ListFiles
import env

from interface import FixEncoding


path: str = f"{env.DOWNLOADS}__TEST__/__eur__/"
fnc: ListFiles = ListFiles("ei")
fnc.update_extensions({".flac", ".mp3"})
files_list: list[str] = fnc(path)

total: int = 0
fixEncoding: FixEncoding = FixEncoding("eur")
for i in files_list:
    fixEncoding.fix(i.name)
