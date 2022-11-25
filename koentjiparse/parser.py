from koentjiutil.cyk import *

GRAMMAR_FILE = 'cfg2.txt'
INPUT_LINES = []
INPUT_RAW = ''

# get -- Membuka file dengan nama filename dan men-drive proses parsing terhadap file tersebut
def get(filename:str) -> None:
    global GRAMMAR_FILE, INPUT_LINES, INPUT_RAW

    cyk = CYK(GRAMMAR_FILE)
    with open(filename) as file:
        INPUT_LINES = file.readlines()
    INPUT_RAW = ''.join(INPUT_LINES)
    
    errline = cyk.parse(INPUT_RAW)
    if errline == 0:
        # Teks valid
        pass
    else:
        # Teks tidak valid
        handleError(errline)

# handleError -- Menghandle error
def handleError(line:int):
    global INPUT_LINES

    print(f'Syntax error on line {line}: ')
    print(INPUT_LINES[line-1])

## parseSyntax -- Mengembalikan 0 jika sintaks js valid, (BONUS: sebaliknya mengembalikan baris yang tidak valid)
#def parseSyntax(f) -> int:
#    return 0
#
## parseExpr -- Mengembalikan True jika ekspresi js valid, sebaliknya False
#def parseExpr(expr:str) -> bool:
#    return True
