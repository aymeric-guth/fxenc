import eur
import jap
import os

# range de détection par module de language
# range de détection globale qui renvoie le language

class FixEncoding(object):
    def __init__(self, language: str):
        if language not in {"jap", "eur"}:
            raise NotImplementedError
        # self.lang = globals()[language]
        self.__dict__.update(globals()[language].__dict__)

    # def fix(self, s: str) -> str:
    #     return self.lang.fix(s=s)

    # def is_invalid(self, s: str) -> str:
    #     return self.lang.is_invalid(s=s)

    def __call__(self, p: os.DirEntry):
        if not isinstance(p, os.DirEntry):
            raise Exception("Méthode supportée pour parametre de type os.DirEntry seulement")
        file_name: str
        extension: str
        file_name, extension = os.path.splitext(p.name)
        path: str = p.path[:-len(p.name)]
        try:
            f = self.fix(file_name)
        except:
            print("Exception")
            print(file_name)
        # src: str = f"{path}{file_name}{extension}"
        # dst: str = f"{path}{f}{extension}"
        # os.rename()
        # print(src)
        # print(dst)
