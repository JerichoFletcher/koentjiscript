from koentjiutil.dfa import *

## DFAs
## 
## Characters
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

# =
dfaEqSign = DFA()
dfaEqSign.acceptLiteral('=')
dfaEqSign.ignore(' ')

# :
dfaColon = DFA()
dfaColon.acceptLiteral(':')
dfaColon.ignore(' ')

# ,
dfaComma = DFA()
dfaComma.acceptLiteral(',')
dfaComma.ignore(' ')

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
dfaIN.start('A')
dfaIN.accept('E')
dfaIN.transition('A', ' ', 'B')
dfaIN.transition('B', ' ', 'B')
dfaIN.transition('B', 'i', 'C')
dfaIN.transition('C', 'n', 'D')
dfaIN.transition('D', ' ', 'E')
dfaIN.transition('E', ' ', 'E')

# OF
dfaOF = DFA()
dfaOF.start('A')
dfaOF.accept('E')
dfaOF.transition('A', ' ', 'B')
dfaOF.transition('B', ' ', 'B')
dfaOF.transition('B', 'o', 'C')
dfaOF.transition('C', 'f', 'D')
dfaOF.transition('D', ' ', 'E')
dfaOF.transition('E', ' ', 'E')

# SWITCH
dfaSWITCH = DFA()
dfaSWITCH.acceptLiteral('switch')

# CASE
dfaCASE = DFA()
dfaCASE.acceptLiteral('case')

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
dfaFUNCTION.acceptLiteral('function ')

# RETURN
dfaRETURN = DFA()
dfaRETURN.acceptLiteral('return')
dfaRETURN.acceptLiteral('return ')

# THROW
dfaTHROW = DFA()
dfaTHROW.acceptLiteral('throw ')

# VAR
dfaVAR = DFA()
dfaVAR.acceptLiteral('var ')

# LET
dfaLET = DFA()
dfaLET.acceptLiteral('let ')

# CONST
dfaCONST = DFA()
dfaCONST.acceptLiteral('const ')

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