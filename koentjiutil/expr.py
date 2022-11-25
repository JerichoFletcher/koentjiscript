from koentjiutil.dfa import *

alphabet = [chr(c) for c in range(ord('a'), ord('z')+1)] + [chr(C) for C in range(ord('A'), ord('Z')+1)]
numeric = [chr(c) for c in range(ord('0'), ord('9')+1)]
sign = '+-' 
ops = '+-*/'
blank = ' '

## DFAs
# (
dfaOpenPar = DFA()
dfaOpenPar.acceptLiteral('(')
dfaOpenPar.ignore(' ')

# )
dfaClosePar = DFA()
dfaClosePar.acceptLiteral(')')
dfaClosePar.ignore(' ')

# {
dfaOpenBracket = DFA()
dfaOpenBracket.acceptLiteral('{')
dfaOpenBracket.ignore(' ')

# }
dfaCloseBracket = DFA()
dfaCloseBracket.acceptLiteral('}')
dfaCloseBracket.ignore(' ')

# ?
dfaQuestion = DFA()
dfaQuestion.acceptLiteral('?')
dfaQuestion.ignore(' ')

# :
dfaColon = DFA()
dfaColon.acceptLiteral(':')
dfaColon.ignore(' ')

# ,
dfaComma = DFA()
dfaComma.acceptLiteral(',')
dfaComma.ignore(' ')

# DFA for operation
dfaOpr = DFA()
dfaOpr.start('q0')
dfaOpr.accept('q1','q2','q7','q8')
dfaOpr.transitions('q0', (alphabet,'q1'),(blank,'q0'),(numeric,'q2'))
dfaOpr.transitions('q1', (alphabet,'q1'), (numeric,'q1'), (ops,'q3'), (blank,'q4'), ('=!', 'q5'),('><','q9'))
dfaOpr.transitions('q2', (numeric,'q2'), (ops,'q3'), (blank,'q4'), ('=!','q5'), ('><','q9'))
dfaOpr.transitions('q3', (alphabet,'q1'), (numeric,'q2'), (blank,'q3'))
dfaOpr.transitions('q4', (blank,'q4'),('=!','q5') ,('><','q9'))
dfaOpr.transitions('q5', ('=', 'q6'), (blank,'q5'))
dfaOpr.transitions('q6', (alphabet,'q7'), (numeric,'q8'),(blank,'q6'))
dfaOpr.transitions('q7', (alphabet,'q7'), (numeric,'q7'),(ops,'q11'), (blank,'q12'))
dfaOpr.transitions('q8', (numeric,'q8'),(ops,'q11'),(blank,'q12'))
dfaOpr.transitions('q9', ('=', 'q10'), (alphabet,'q7'), (numeric,'q8'), (blank,'q9'))
dfaOpr.transitions('q10', (blank,'q10'), (alphabet,'q7'), (numeric,'q8'))
dfaOpr.transitions('q11', (blank,'q11'), (alphabet,'q7'), (numeric,'q8'))
dfaOpr.transitions('q12', (blank,'q12'), (ops,'q11'))

# Line terminator
dfaLT = DFA()
dfaLT.start('A')
dfaLT.accept('B')
dfaLT.transitions('A', (';\n', 'B'))
dfaLT.transitions('B', (';\n', 'B'))
dfaLT.kstarBefore(' ')
dfaLT.kstarAfter(' ')

# Assignment operators
dfaASSIGN = DFA()
dfaASSIGN.start('A')
dfaASSIGN.accept('End')
dfaASSIGN.transitions('A', ('=', 'End'), ('+-/%', 'B'), ('*', 'C'))
dfaASSIGN.transitions('B', ('=', 'End'))
dfaASSIGN.transitions('C', ('=', 'End'), ('*', 'D'))
dfaASSIGN.transitions('D', ('=', 'End'))
dfaASSIGN.kstarBefore(' ')
dfaASSIGN.kstarAfter(' ')

# Prefix unary operators
dfaUNOPPRE = DFA()
dfaUNOPPRE.acceptLiteral('++')
dfaUNOPPRE.acceptLiteral('--')
dfaUNOPPRE.acceptLiteral('!')
dfaUNOPPRE.acceptLiteral('~')
dfaUNOPPRE.kstarBefore(' ')
dfaUNOPPRE.kstarAfter(' ')

# Postfix unary operators
dfaUNOPPOS = DFA()
dfaUNOPPOS.acceptLiteral('++')
dfaUNOPPOS.acceptLiteral('--')
dfaUNOPPOS.kstarBefore(' ')
dfaUNOPPOS.kstarAfter(' ')

# Binary operators
dfaBINOP = DFA()
dfaBINOP.start('A')
dfaBINOP.accept('End', 'C', 'E', 'Fa', 'Fb', 'Fbb', 'G', 'H')
dfaBINOP.transitions('A', ('+-/%^', 'End'), ('*', 'C'))
dfaBINOP.transitions('A', ('=!', 'D'), ('<', 'Fa'), ('>', 'Fb'), ('&', 'G'), ('|', 'H'))
dfaBINOP.transitions('C', ('*', 'End'))
dfaBINOP.transitions('D', ('=', 'E'))
dfaBINOP.transitions('E', ('=', 'End'))
dfaBINOP.transitions('Fa', ('=<', 'End'))
dfaBINOP.transitions('Fb', ('=', 'End'), ('>', 'Fbb'))
dfaBINOP.transitions('Fbb', ('>', 'End'))
dfaBINOP.transitions('G', ('&', 'End'))
dfaBINOP.transitions('H', ('|', 'End'))
dfaBINOP.kstarBefore(' ')
dfaBINOP.kstarAfter(' ')

# IF
dfaIF = DFA()
dfaIF.acceptLiteral('if')

# ELSE
dfaELSE = DFA()
dfaELSE.acceptLiteral('else')

# FOR
dfaFOR = DFA()
dfaFOR.acceptLiteral('for')

# WHILE
dfaWHILE  = DFA()
dfaWHILE.acceptLiteral('while')

# BREAK
dfaBREAK = DFA()
dfaBREAK.acceptLiteral('break')

# CONTINUE
dfaCONTINUE = DFA()
dfaCONTINUE.acceptLiteral('continue')

# IN
dfaIN = DFA()
dfaIN.acceptLiteral('in')
dfaIN.kplusBefore(' ')
dfaIN.kplusAfter(' ')
#dfaIN.start('A')
#dfaIN.accept('E')
#dfaIN.transition('A', ' ', 'B')
#dfaIN.transition('B', ' ', 'B')
#dfaIN.transition('B', 'i', 'C')
#dfaIN.transition('C', 'n', 'D')
#dfaIN.transition('D', ' ', 'E')
#dfaIN.transition('E', ' ', 'E')

# OF
dfaOF = DFA()
dfaOF.acceptLiteral('of')
dfaOF.kplusBefore(' ')
dfaOF.kplusAfter(' ')
#dfaOF.start('A')
#dfaOF.accept('E')
#dfaOF.transition('A', ' ', 'B')
#dfaOF.transition('B', ' ', 'B')
#dfaOF.transition('B', 'o', 'C')
#dfaOF.transition('C', 'f', 'D')
#dfaOF.transition('D', ' ', 'E')
#dfaOF.transition('E', ' ', 'E')

# SWITCH
dfaSWITCH = DFA()
dfaSWITCH.acceptLiteral('switch')

# CASE
dfaCASE = DFA()
dfaCASE.acceptLiteral('case')
dfaCASE.kplusAfter(' ')

# DEFAULT
dfaDEFAULT = DFA()
dfaDEFAULT.acceptLiteral('default')

# TRY
dfaTRY = DFA()
dfaTRY.acceptLiteral('try')

# CATCH
dfaCATCH = DFA()
dfaCATCH.acceptLiteral('catch')

# FINALLY
dfaFINALLY = DFA()
dfaFINALLY.acceptLiteral('finally')

# FUNCTION
dfaFUNCTION = DFA()
dfaFUNCTION.acceptLiteral('function')
dfaFUNCTION.kplusAfter(' ')

# RETURN
dfaRETURN = DFA()
dfaRETURN.acceptLiteral('return')

# RETURNVAL
dfaRETURNVAL = DFA()
dfaRETURNVAL.acceptLiteral('return')
dfaRETURNVAL.kplusAfter(' ')

# THROW
dfaTHROW = DFA()
dfaTHROW.acceptLiteral('throw')
dfaTHROW.kplusAfter(' ')

# VAR
dfaVAR = DFA()
dfaVAR.acceptLiteral('var')
dfaVAR.kplusAfter(' ')

# LET
dfaLET = DFA()
dfaLET.acceptLiteral('let')
dfaLET.kplusAfter(' ')

# CONST
dfaCONST = DFA()
dfaCONST.acceptLiteral('const')
dfaCONST.kplusAfter(' ')

# ID
dfaID = DFA()
dfaID.start('A')
dfaID.accept('B')
dfaID.transitions('A', (alphabet, 'B'))
dfaID.transitions('B', (alphabet + numeric + ['.', '_'], 'B'))
dfaID.kstarBefore(' ')

# NUM
dfaNUM = DFA()
dfaNUM.acceptLiteral('num')

# STR
dfaSTR = DFA()
dfaSTR.acceptLiteral('str')

# ARR
dfaARR = DFA()
dfaARR.acceptLiteral('arr')

EXPRESSIONS = {
    "'IF'": dfaIF,
    "'ELSE'": dfaELSE,
    "'FOR'": dfaFOR,
    "'WHILE'": dfaWHILE,
    "'BREAK'": dfaBREAK,
    "'CONTINUE'": dfaCONTINUE,
    "'IN'": dfaIN,
    "'OF'": dfaOF,
    "'SWITCH'": dfaSWITCH,
    "'CASE'": dfaCASE,
    "'DEFAULT'": dfaDEFAULT,
    "'TRY'": dfaTRY,
    "'CATCH'": dfaCATCH,
    "'FINALLY'": dfaFINALLY,
    "'FUNCTION'": dfaFUNCTION,
    "'RETURN'": dfaRETURN,
    "'RETURNVAL'": dfaRETURNVAL,
    "'THROW'": dfaTHROW,
    "'VAR'": dfaVAR,
    "'LET'": dfaLET,
    "'CONST'": dfaCONST,
    "'ID'": dfaID,
    "'NUM'": dfaNUM,
    "'STR'": dfaSTR,
    "'ARR'": dfaARR,
    "'('": dfaOpenPar,
    "')'": dfaClosePar,
    "'{'": dfaOpenBracket,
    "'}'": dfaCloseBracket,
    "'?'": dfaQuestion,
    "':'": dfaColon,
    "','": dfaComma,
    "'LT'": dfaLT,
    "'ASSIGN_OP'": dfaASSIGN,
    "'UN_OP_PRE'": dfaUNOPPRE,
    "'UN_OP_POS'": dfaUNOPPOS,
    "'BIN_OP'": dfaBINOP
}

class Node:
    # Konstruktor
    def __init__(self, term:str, line:int) -> None:
        self._term = term
        self._line = line
    
    def __repr__(self) -> str:
        return f'{self._line}:{self._term}'

# exprConvert -- Mengubah string menjadi list[Node]
def exprConvert(inp:str) -> tuple[int, list]:
    result:list[Node] = []
    line = 1

    def resetAll():
        for dfa in EXPRESSIONS.values(): dfa.begin()
    resetAll()

    def process(ch, l):
        line = l
        active = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isActive()]
        accept = [(key, dfa) for key, dfa in active if dfa.isAccepted()]
        #activeKeys = [key for key, _ in active]
        #print(f'{ch}: {activeKeys}')
        if len(active) == 0:
            # Syntax error
            return True, line
        elif len(accept) == 1:
            # Sisa 1 DFA aktif, convert
            key, dfa = accept[0]
            for _, dfa in active:
                dfa.step(ch)

            active = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isActive()]
            if not dfa.isActive() and len(active) == 0:
                #print(f'Adding {key} to result')
                node = Node(key, line)
                result.append(node)

                resetAll()
                active = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isActive()]
                for _, dfa in active: dfa.step(ch)
        else:
            # Sisa banyak DFA aktif, langkah
            for _, dfa in active:
                dfa.step(ch)
        if ch == '\n': line += 1
        return False, line

    for ch in inp:
        err, line = process(ch, line)
        if err: break
    if not err: err, line = process(inp[len(inp)-1], line)
    
    return 0 if not err else line, result
