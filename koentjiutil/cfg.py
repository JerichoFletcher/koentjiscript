from koentjiutil.util_dict import *

# Class CFG
class CFG:
    # Konstruktor
    def __init__(self, start:str, grammar:str) -> None:
        self._productions:dict[str, list[list[str]]] = {}
        self._start:str = start
        self.load(grammar)
        self.toCNF()
    
    # load -- Membuka file dan meload semua production rule ke dalam memori
    def load(self, grammar:str) -> None:
        with open(grammar) as file:
            lines = file.readlines()
        for line in [line.replace('->', '').split() for line in lines]:
            if len(line) == 0 or line[0] == '#':
                continue
            dict_add_nondup(self._productions, line[0], line[1:])
    
    # toCNF -- Mengubah CFG ke dalam bentuk CNF
    def toCNF(self) -> None:
        result = {}

        # Iterasi setiap rule dalam grammar
        idx = 0
        unit = []
        for key, val in self._productions.items():
            new_prods = []
            for prod in val:
                if len(prod) == 1 and prod[0][0] != "'":
                    # Keep track unit production untuk dihandle terakhir
                    unit.append((key, prod))
                    continue
                elif len(prod) >= 2:
                    # Cari semua terminal dalam production, ganti dengan nonterminal baru
                    for i in range(len(prod)):
                        x = prod[i]
                        if x[0] == "'":
                            new_nonterm = f'{key}{str(idx)}'
                            prod[i] = new_nonterm
                            new_prods.append((new_nonterm, [x]))
                            idx += 1
                    
                    # Semua suku RHS dari production terdiri atas nonterminal
                    # Jika terdapat lebih dari 2 nonterminal, gantikan 2 nonterminal pertama dengan nonterminal baru
                    while len(prod) > 2:
                        new_nonterm = f'{key}{str(idx)}'
                        new_prods.append((new_nonterm, [prod[0], prod[1]]))
                        prod = [new_nonterm] + prod[2:]
                        idx += 1
                
                # Production terdiri atas 2 nonterminal atau 1 terminal
                # Sudah valid, simpan semua production yang dihasilkan
                dict_add_nondup(result, key, prod)
                for new_key, new_prod in new_prods:
                    dict_add_nondup(result, new_key, new_prod)
        
        k = 0
        while k < len(list(result.keys())):
            key = list(result.keys())[i]
            val = result[key]
            k += 1

            new_prods = []
            for prod in val:
                if len(prod) == 1 and prod[0][0] != "'":
                    # Keep track unit production untuk dihandle terakhir
                    if not (key, prod) in unit:
                        unit.append((key, prod))
                    continue
                elif len(prod) >= 2:
                    # Cari semua terminal dalam production, ganti dengan nonterminal baru
                    for i in range(len(prod)):
                        x = prod[i]
                        if x[0] == "'":
                            new_nonterm = f'{key}{str(idx)}'
                            prod[i] = new_nonterm
                            new_prods.append((new_nonterm, [x]))
                            idx += 1
                    
                    # Semua suku RHS dari production terdiri atas nonterminal
                    # Jika terdapat lebih dari 2 nonterminal, gantikan 2 nonterminal pertama dengan nonterminal baru
                    while len(prod) > 2:
                        new_nonterm = f'{key}{str(idx)}'
                        new_prods.append((new_nonterm, [prod[0], prod[1]]))
                        prod = [new_nonterm] + prod[2:]
                        idx += 1
                
                # Production terdiri atas 2 nonterminal atau 1 terminal
                # Sudah valid, simpan semua production yang dihasilkan
                for new_key, new_prod in new_prods:
                    dict_add_nondup(result, new_key, new_prod)
        
        # Handle unit production
        while len(unit) > 0:
            key, val = unit.pop()
            #print(f'Next processing: {key} -> {val}')
            if val[0] in result.keys() and val[0] not in [key for key, _ in unit]:
                for ext_prod in result[val[0]]:
                    if len(ext_prod) == 1 and ext_prod[0][0] != "'":
                        # Production ini juga unit production, tambahkan ke queue
                        #print(f'  Queueing {prod[0]} -> {ext_prod}')
                        unit.append((prod[0], ext_prod))
                    else:
                        # Production ini bukan unit production, simpan
                        #print(f'  Adding {key} -> {ext_prod}')
                        dict_add_nondup(result, key, ext_prod)
            else:
                #print(f'  Processing later')
                unit.insert(0, (key, val))
        
        # Simpan hasil sebagai production rule yang baru
        self._productions.clear()
        self._productions = result

    def __repr__(self) -> str:
        repr = ''
        for key in self._productions.keys():
            for val in self._productions[key]:
                repr += f'{key} ->'
                for i in range(len(val)):
                    repr += f' {val[i]}'
                repr += '\n'
        return repr