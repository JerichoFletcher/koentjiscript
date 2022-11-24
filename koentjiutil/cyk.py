from koentjiutil.cfg import *
from koentjiutil.expr import *

# Class CYK
class CYK:
    # Konstruktor
    def __init__(self, grammar:str) -> None:
        self._cfg = CFG('S', grammar)

    # parse -- Menerima input teks raw dan mengembalikan 0 jika teks valid, sebaliknya mengembalikan baris yang error
    def parse(self, inp:str) -> int:
        errline, terms = exprConvert(inp)
        if errline == 0:
            # Proses di sini
            return 0
        else:
            return errline
