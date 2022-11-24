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
