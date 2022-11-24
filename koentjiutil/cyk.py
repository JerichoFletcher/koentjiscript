from koentjiutil.cfg import *

# Class CYK
class CYK:
    # Konstruktor
    def __init__(self, grammar:str) -> None:
        self._cfg = CFG('S', grammar)

    # parse -- Menerima ??? dan mengembalikan ???
    def parse(self, inp:str):
        for i, ch in enumerate(inp):
            print(f'{i}:{ch}', end='')
