from koentjiutil.cfg import *
from koentjiutil.expr import *

# Class CYK
class CYK:
    # Konstruktor
    def __init__(self, grammar:str) -> None:
        self._cfg = CFG('S', grammar)
        #print(self._cfg)

    # parse -- Menerima input teks raw dan mengembalikan 0 jika teks valid, sebaliknya mengembalikan baris yang error
    def parse(self, inp:str) -> int:
        errline, terms = exprConvert(inp)
        #print(terms)
        if errline == 0:
            # Proses di sini
            n = len(terms)

            Table = [[set([]) for j in range(n)] for i in range (n)]
            for i in range(0,n):
                for left, rule in self._cfg._productions.items():
                    for right in rule:
                        if len(right) == 1 and right[0] == terms[i]._term:
                            Table[i][i].add(left)
            for j in range(1,n):
                for i in range(n-j-1,-1,-1):
                    x, y = i, i+j
                    a, b = i, i
                    c, d = i+1, y
                    while c <= d:
                        for left, rule in self._cfg._productions.items():
                            for right in rule:
                                if len(right) == 2 and right[0] in Table[a][b] and right[1] in Table[c][d]:
                                    Table[x][y].add(left)
                        a, b = a, b+1
                        c, d = c+1, d
                    
                #for i in range(j,-1,-1):
                #    for count in range(i,j+1):
                #        for left,rule in self._cfg._productions.items():
                #            for right in rule:
                #                if len(right) == 2 and right[0] in Table[i][count] and right[1] in Table[count][j]:
                #                    Table[i][j].add(left)
            for i in range(n):
                for j in range(n):
                    toWrite = str(Table[i][j] if len(Table[i][j]) > 0 else '{}')
                    print(toWrite + ' ' * (32 - len(toWrite)), end='')
                print()

            print(Table[0][n-1])
            if len(Table[0][n-1]) != 0:
            #if self._cfg._start in Table[0][n-1]:
                print("Accepted")
            else:
                print("Syntax error")
            return 0
        else:
            return errline
