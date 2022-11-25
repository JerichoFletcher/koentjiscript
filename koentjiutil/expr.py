from koentjiutil.dfa import *

any = ''.join([chr(c) for c in range(0, 256)])
any_nosinglequote = ''.join([c for c in any if c != "'"])
any_nodoublequote = ''.join([c for c in any if c != '"'])

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric = '0123456789'
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

# [
dfaOpenBrace = DFA()
dfaOpenBrace.acceptLiteral('[')
dfaOpenBrace.ignore(' ')

# ]
dfaCloseBrace = DFA()
dfaCloseBrace.acceptLiteral(']')
dfaCloseBrace.ignore(' ')

# ?
dfaQuestion = DFA()
dfaQuestion.acceptLiteral('?')
dfaQuestion.ignore(' ')

# :
dfaColon = DFA()
dfaColon.acceptLiteral(':')
dfaColon.ignore(' ')

# .
dfaDot = DFA()
dfaDot.acceptLiteral('.')
dfaDot.ignore(' ')

# ,
dfaComma = DFA()
dfaComma.acceptLiteral(',')
dfaComma.ignore(' ')

#
#  DFA for operation
#dfaOpr = DFA()
#dfaOpr.start('q0')
#dfaOpr.accept('q1','q2','q7','q8')
#dfaOpr.transitions('q0', (alphabet,'q1'),(blank,'q0'),(numeric,'q2'))
#dfaOpr.transitions('q1', (alphabet,'q1'), (numeric,'q1'), (ops,'q3'), (blank,'q4'), ('=!', 'q5'),('><','q9'))
#dfaOpr.transitions('q2', (numeric,'q2'), (ops,'q3'), (blank,'q4'), ('=!','q5'), ('><','q9'))
#dfaOpr.transitions('q3', (alphabet,'q1'), (numeric,'q2'), (blank,'q3'))
#dfaOpr.transitions('q4', (blank,'q4'),('=!','q5') ,('><','q9'))
#dfaOpr.transitions('q5', ('=', 'q6'), (blank,'q5'))
#dfaOpr.transitions('q6', (alphabet,'q7'), (numeric,'q8'),(blank,'q6'))
#dfaOpr.transitions('q7', (alphabet,'q7'), (numeric,'q7'),(ops,'q11'), (blank,'q12'))
#dfaOpr.transitions('q8', (numeric,'q8'),(ops,'q11'),(blank,'q12'))
#dfaOpr.transitions('q9', ('=', 'q10'), (alphabet,'q7'), (numeric,'q8'), (blank,'q9'))
#dfaOpr.transitions('q10', (blank,'q10'), (alphabet,'q7'), (numeric,'q8'))
#dfaOpr.transitions('q11', (blank,'q11'), (alphabet,'q7'), (numeric,'q8'))
#dfaOpr.transitions('q12', (blank,'q12'), (ops,'q11'))

# Line terminator
dfaLT = DFA()
dfaLT.start('A')
dfaLT.accept('B', 'C')
dfaLT.transitions('A', ('\n', 'B'), (';', 'C'))
dfaLT.transitions('B', (';\n', 'B'))
dfaLT.transitions('C', ('\n', 'B'))
dfaLT.ignore(' ')

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
dfaIF.kstarBefore(' ')
dfaIF.kstarAfter(' ')

# ELSE
dfaELSE = DFA()
dfaELSE.acceptLiteral('else')
dfaELSE.kstarBefore(' ')
dfaELSE.kstarAfter(' ')

# ELSEIF
dfaELSEIF = DFA()
dfaELSEIF.acceptLiteral('else ')
dfaELSEIF.kstarBefore(' ')
dfaELSEIF.transitions('else 5', ('i', 'I'), (' \n', 'else 5'))
dfaELSEIF.transitions('I', ('f', 'F'))
dfaELSEIF._accept.clear()
dfaELSEIF.accept('F')
dfaELSEIF.kstarAfter(' ')

# FOR
dfaFOR = DFA()
dfaFOR.acceptLiteral('for')
dfaFOR.kstarBefore(' ')
dfaFOR.kstarAfter(' ')

# WHILE
dfaWHILE  = DFA()
dfaWHILE.acceptLiteral('while')
dfaWHILE.kstarBefore(' ')
dfaWHILE.kstarAfter(' ')

# BREAK
dfaBREAK = DFA()
dfaBREAK.acceptLiteral('break')
dfaBREAK.kstarBefore(' ')
dfaBREAK.kstarAfter(' ')

# CONTINUE
dfaCONTINUE = DFA()
dfaCONTINUE.acceptLiteral('continue')
dfaCONTINUE.kstarBefore(' ')
dfaCONTINUE.kstarAfter(' ')

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
dfaSWITCH.kstarBefore(' ')
dfaSWITCH.kstarAfter(' ')

# CASE
dfaCASE = DFA()
dfaCASE.acceptLiteral('case')
dfaCASE.kstarBefore(' ')
dfaCASE.kplusAfter(' ')

# DEFAULT
dfaDEFAULT = DFA()
dfaDEFAULT.acceptLiteral('default')
dfaDEFAULT.kstarBefore(' ')
dfaDEFAULT.kstarAfter(' ')

# TRY
dfaTRY = DFA()
dfaTRY.acceptLiteral('try')
dfaTRY.kstarBefore(' ')
dfaTRY.kstarAfter(' ')

# CATCH
dfaCATCH = DFA()
dfaCATCH.acceptLiteral('catch')
dfaCATCH.kstarBefore(' ')
dfaCATCH.kstarAfter(' ')

# FINALLY
dfaFINALLY = DFA()
dfaFINALLY.acceptLiteral('finally')
dfaFINALLY.kstarBefore(' ')
dfaFINALLY.kstarAfter(' ')

# FUNCTION
dfaFUNCTION = DFA()
dfaFUNCTION.acceptLiteral('function')
dfaFUNCTION.kstarBefore(' ')
dfaFUNCTION.kplusAfter(' ')

# RETURN
dfaRETURN = DFA()
dfaRETURN.acceptLiteral('return')
dfaRETURN.kstarBefore(' ')
dfaRETURN.kstarAfter(' ')

# RETURNVAL
dfaRETURNVAL = DFA()
dfaRETURNVAL.acceptLiteral('return')
dfaRETURNVAL.kstarBefore(' ')
dfaRETURNVAL.kplusAfter(' ')

# THROW
dfaTHROW = DFA()
dfaTHROW.acceptLiteral('throw')
dfaTHROW.kstarBefore(' ')
dfaTHROW.kplusAfter(' ')

# VAR
dfaVAR = DFA()
dfaVAR.acceptLiteral('var')
dfaVAR.kstarBefore(' ')
dfaVAR.kplusAfter(' ')

# LET
dfaLET = DFA()
dfaLET.acceptLiteral('let')
dfaLET.kstarBefore(' ')
dfaLET.kplusAfter(' ')

# CONST
dfaCONST = DFA()
dfaCONST.acceptLiteral('const')
dfaCONST.kstarBefore(' ')
dfaCONST.kplusAfter(' ')

# ID
dfaID = DFA()
dfaID.start('A')
dfaID.accept('B')
dfaID.transitions('A', (alphabet, 'B'))
dfaID.transitions('B', (alphabet + numeric + '._', 'B'))
dfaID.kstarBefore(' ')
dfaID.kstarAfter(' ')

# NUM
dfaNUM = DFA()
dfaNUM.start('A')
dfaNUM.accept('B', 'C')
dfaNUM.transitions('A', (numeric, 'B'), ('.', 'C'))
dfaNUM.transitions('B', (numeric, 'B'), ('.', 'C'))
dfaNUM.transitions('C', (numeric, 'C'))
dfaNUM.kstarBefore(' ')
dfaNUM.kstarAfter(' ')

# STR
dfaSTR = DFA()
dfaSTR.start('A')
dfaSTR.accept('End')
dfaSTR.transitions('A', ("'", 'Single'), ('"', 'Double'))
dfaSTR.transitions('Single', (any_nosinglequote, 'Single'), ("'", 'End'))
dfaSTR.transitions('Double', (any_nodoublequote, 'Double'), ('"', 'End'))
dfaSTR.kstarBefore(' ')
dfaSTR.kstarAfter(' ')

EXPRESSIONS = {
    "'IF'": dfaIF,
    "'ELSEIF'": dfaELSEIF,
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
    "'('": dfaOpenPar,
    "')'": dfaClosePar,
    "'{'": dfaOpenBracket,
    "'}'": dfaCloseBracket,
    "'['": dfaOpenBrace,
    "']'": dfaCloseBrace,
    "'?'": dfaQuestion,
    "':'": dfaColon,
    #"'.'": dfaDot,
    "','": dfaComma,
    "'LT'": dfaLT,
    "'ASSIGN_OP'": dfaASSIGN,
    "'UN_OP_PRE'": dfaUNOPPRE,
    "'UN_OP_POS'": dfaUNOPPOS,
    "'BIN_OP'": dfaBINOP
}

NON_KEYWORDS = ["'ID'", "'NUM'", "'STR'"]

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

    def process(string:str, startIdx:int) -> tuple[bool, tuple[str, int]]:
        maxLen:dict[str, tuple[bool, int]] = {key: (False, 0) for key, _ in EXPRESSIONS.items()}
        for key, dfa in EXPRESSIONS.items():
            dfa.begin()
            i = startIdx
            while i < len(string) and dfa.isActive():
                #print(f'{string[i]} -> {key}')
                accepted = dfa.isAccepted()
                dfa.step(string[i])
                if dfa.isActive():
                    if i == len(string) - 1:
                        maxLen[key] = (dfa.isAccepted(), maxLen[key][1] + 1)
                        break
                    else:
                        maxLen[key] = (maxLen[key][0], maxLen[key][1] + 1)
                else:
                    maxLen[key] = (accepted, maxLen[key][1])
                    break
                i += 1
        max = (None, 0)
        maxID = (None, 0)
        for key, num in maxLen.items():
            #print(f'{key} consumed {num}')
            if key != "'ID'" and num[0] and max[1] < num[1]:
                max = (key, num[1])
            elif key == "'ID'":
                maxID = (key, num[1])
        if maxID[0] == None:
            return True, (None, 0)
        else:
            return (False, maxID) if maxID[1] > max[1] else (False, max)
            #return (False, max) if max[0] != None else (False, maxID)
        

    #def process(ch, l, lastChar):
    #    line = l
    #    active = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isActive()]
    #    accept = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isAccepted()]
    #    #print(f'{ord(ch)}: ')
    #    if len(active) == 0:
    #        # Syntax error
    #        return True, line
    #    elif len(accept) == 1:
    #        # Sisa 1 DFA aktif, convert
    #        key, dfa = accept[0]
    #        for _, dfa in active:
    #            dfa.step(ch)
    #
    #        active = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isActive()]
    #        #activeKeys = [key for key, _ in active]
    #        #acceptKeys = [key for key, _ in accept]
    #        #print(f'{activeKeys} {acceptKeys}')
    #        if (lastChar and len(accept) == 1) or (not dfa.isActive() and len(active) == 0):
    #            #print(f'Adding {key} to result')
    #            node = Node(key, line // 2 + 1)
    #            result.append(node)
    #
    #            resetAll()
    #            active = [(key, dfa) for key, dfa in EXPRESSIONS.items() if dfa.isActive()]
    #            for _, dfa in active: dfa.step(ch)
    #    else:
    #        # Sisa banyak DFA aktif, langkah
    #        for _, dfa in active:
    #            dfa.step(ch)
    #    if ch == '\n': line += 1
    #    return False, line

    #for ch in inp:
    #    err, line = process(ch, line, False)
    #    if err: break
    #if len(inp) > 0 and not err: err, line = process(inp[len(inp)-1], line, True)

    i = 0
    while i < len(inp):
        #print(f'{i}/{len(inp)-1}: {inp[i]}')
        #print(f'{i}/{len(inp)}')
        err, node = process(inp, i)
        #print(err, node)
        #print(err, node)
        if err: return (line, result)
        jump = node[1]
        while jump > 0:
            i += 1
            jump -= 1
            if i >= len(inp): break
            if inp[i] == '\n': line += 1
        node = Node(node[0], line)
        result.append(node)
    
    return (0, result)
