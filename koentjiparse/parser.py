from koentjiutil.cyk import *

GRAMMAR_FILE = 'cfg.txt'

# get -- Membuka file dengan nama filename dan men-drive proses parsing terhadap file tersebut
def get(filename:str) -> None:
    parser = CYK(GRAMMAR_FILE)
    return

# parseSyntax -- Mengembalikan 0 jika sintaks js valid, (BONUS: sebaliknya mengembalikan baris yang tidak valid)
def parseSyntax(f) -> int:
    return 0

# parseExpr -- Mengembalikan True jika ekspresi js valid, sebaliknya False
def parseExpr(expr:str) -> bool:
    return True
