from koentjiutil.cfg import *

# Class CYK
class CYK:
    # Konstruktor
    def __init__(self, grammar:str) -> None:
        self._cfg = CFG(grammar)

    # parse -- Menerima ??? dan mengembalikan ???
    def parse(self):
        pass
