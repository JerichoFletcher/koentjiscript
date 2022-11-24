from koentjiutil.dfa import *

# DFAs
# (
dfaOpenPar = DFA()
dfaOpenPar.start('A')
dfaOpenPar.accept('B')
dfaOpenPar.transitions('A', ('(', 'B'))
dfaOpenPar.ignore(' ')

# )
dfaClosePar = DFA()
dfaClosePar.start('A')
dfaClosePar.accept('B')
dfaClosePar.transitions('A', (')', 'B'))
dfaClosePar.ignore(' ')

# {
dfaOpenBraces = DFA()
dfaOpenBraces.start('A')
dfaOpenBraces.accept('B')
dfaOpenBraces.transitions('A', ('{', 'B'))
dfaOpenBraces.ignore(' ')

# }
dfaCloseBraces = DFA()
dfaCloseBraces.start('A')
dfaCloseBraces.accept('B')
dfaCloseBraces.transitions('A', ('}', 'B'))
dfaCloseBraces.ignore(' ')

# LT
dfaLT = DFA()
dfaLT.start('A')
dfaLT.accept('B')
dfaLT.transitions('A', (';\n', 'B'))

