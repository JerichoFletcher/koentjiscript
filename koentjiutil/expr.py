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