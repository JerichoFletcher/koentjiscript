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
