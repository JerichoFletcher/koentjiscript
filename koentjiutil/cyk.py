from koentjiutil.cfg import *

# Class CYK
class CYK:
    def __init__(self, grammar:str) -> None:
        self._cfg = CFG(grammar)
        print(self._cfg, end='')

# cykParse -- Menerima input string dan CFG, mengembalikan ??? jika string diterima oleh bahasa CFG, sebaliknya ???
#def cykParse(toParse:str, grammar:CFG) -> any:
#    return None
