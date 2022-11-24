from koentjiutil.dfa import *

## DFAs
# (
dfaOpenPar = DFA()
dfaOpenPar.acceptLiteral('(')
dfaOpenPar.ignore(' \n')

# )
dfaClosePar = DFA()
dfaClosePar.acceptLiteral(')')
dfaClosePar.ignore(' \n')

# {
dfaOpenBracket = DFA()
dfaOpenBracket.acceptLiteral('{')
dfaOpenBracket.ignore(' \n')

# }
dfaCloseBracket = DFA()
dfaCloseBracket.acceptLiteral('}')
dfaCloseBracket.ignore(' \n')

# ?
dfaQuestion = DFA()
dfaQuestion.acceptLiteral('?')
dfaQuestion.ignore(' \n')

# :
dfaColon = DFA()
dfaColon.acceptLiteral(':')
dfaColon.ignore(' \n')

# ,
dfaComma = DFA()
dfaComma.acceptLiteral(',')
dfaComma.ignore(' \n')

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

dfaVar = DFA()
dfaVar.start('A')
dfaVar.accept('B')
dfaVar.transitions('A', (alphabet,'B'), (blank,'A'))
dfaVar.transitions('B', (blank,'A'))

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
dfaBINOP.acceptLiteral('typeof')
dfaBINOP.acceptLiteral('instanceof')
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
dfaID.acceptLiteral('id')

# NUM
dfaNUM = DFA()
dfaNUM.acceptLiteral('num')

# STR
dfaSTR = DFA()
dfaSTR.acceptLiteral('str')

# ARR
dfaARR = DFA()
dfaSTR.acceptLiteral('arr')
dfaComma.ignore(' \n')

EXPRESSIONS = {
    'IF': dfaIF,
    'ELSE': dfaELSE,
    'FOR': dfaFOR,
    'WHILE': dfaWHILE,
    'BREAK': dfaBREAK,
    'CONTINUE': dfaCONTINUE,
    'IN': dfaIN,
    'OF': dfaOF,
    'SWITCH': dfaSWITCH,
    'CASE': dfaCASE,
    'DEFAULT': dfaDEFAULT,
    'TRY': dfaTRY,
    'CATCH': dfaCATCH,
    'FINALLY': dfaFINALLY,
    'FUNCTION': dfaFUNCTION,
    'RETURN': dfaRETURN,
    'RETURNVAL': dfaRETURNVAL,
    'THROW': dfaTHROW,
    'VAR': dfaVAR,
    'LET': dfaLET,
    'CONST': dfaCONST,
    'ID': dfaID,
    'NUM': dfaNUM,
    'STR': dfaSTR,
    'ARR': dfaARR,
    '(': dfaOpenPar,
    ')': dfaClosePar,
    '{': dfaOpenBracket,
    '}': dfaCloseBracket,
    '?': dfaQuestion,
    ':': dfaColon,
    ',': dfaComma,
    'LT': dfaLT,
    'ASSIGN_OP': dfaASSIGN,
    'UN_OP_PRE': dfaUNOPPRE,
    'UN_OP_POS': dfaUNOPPOS,
    'BIN_OP': dfaBINOP
}
