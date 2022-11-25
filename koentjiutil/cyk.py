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
            n = len(terms)

            Table = [[set([]) for j in range(n)] for i in range (n)]
            for j in range(0,n):
                for left, rule in self._cfg:
                    for right in rule:
                        if len(right) == 1 and right[0] == terms[j]:
                            Table[j][j].add(left)
            for i in range(j,-1,-1):
                for count in range(i,j+1):
                    for left,rule in self._cfg:
                        for right in rule:
                            if len(right) == 2 and right[0] in Table[i][count] and right[1] in Table[count+1][j]:
                                Table[i][j].add(left)
            if len(Table[0][n-1]) != 0:
                print("Accepted")
            else:
                print("Syntax error")
            return 0
        else:
            return errline
