# Class CFG
class CFG:
    # Konstruktor
    def __init__(self, grammar:str) -> None:
        self._productions = {}
        self._load(grammar)
    
    def _load(self, grammar:str) -> None:
        with open(grammar) as file:
            lines = file.readlines()
        for line in [line.replace('->', '').split() for line in lines]:
            if len(line) == 0 or line[0] == '#':
                continue
            if line[0] not in self._productions.keys():
                self._productions[line[0]] = []
            self._productions[line[0]].append(line[1:])

    def __repr__(self) -> str:
        repr = ''
        for key in self._productions.keys():
            for val in self._productions[key]:
                repr += f'{key} ->'
                for i in range(len(val)):
                    repr += f' {val[i]}'
                repr += '\n'
        return repr
