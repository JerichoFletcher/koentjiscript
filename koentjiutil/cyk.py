from koentjiutil.cfg import *
from koentjiutil.expr import *

# Class CYK
class CYK:
    # Konstruktor
    def __init__(self, grammar:str) -> None:
        self._cfg = CFG('S', grammar)

    # parse -- Menerima ??? dan mengembalikan ???
    def parse(self, inp:str) -> tuple[int, bool]:
        errline, terms = exprConvert(inp)
        if errline == 0:
            # Proses di sini
            return 0, True
        else:
            return errline, False
