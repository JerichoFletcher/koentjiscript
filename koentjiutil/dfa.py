# Class DFA
from typing import Tuple

class DFA:
    # Konstruktor
    def __init__(self):
        self._states = []
        self._accept = []
        self._delta = {}
        self._start = None
        self._ignore = ''

    # get -- Menerima input string dan mengembalikan True jika string diterima oleh DFA, sebaliknya False
    def get(self, inp:str) -> bool:
        x = self._start
        self.currentState = self._start
        for c in inp:
            if c in self._ignore: continue
            if c not in self._delta[x]: return False
            x = self._delta[x][c]
        return x in self._accept

    # state -- Menambahkan state baru ke DFA
    def state(self, name:str):
        if name not in self._states: self._states.append(name)

    # transition -- Menambahkan satu fungsi transisi baru ke DFA
    def transition(self, stateFrom:str, inp:str, stateTo:str):
        if len(inp) > 1:
            for c in inp: self.transition(stateFrom, c, stateTo)
            return

        if stateFrom not in self._delta.keys():
            self._delta[stateFrom] = {}

        if inp in self._delta[stateFrom].keys() is not None:
            print(f'Transition function for {self} already has the transition ({stateFrom}, {inp}) -> {self._delta[stateFrom][inp]}; overwriting with {stateTo}.')
        
        self._delta[stateFrom][inp] = stateTo
        self.state(stateFrom)
        self.state(stateTo)

    # transitions -- Menambahkan banyak fungsi transisi baru dari satu state ke DFA
    def transitions(self, stateFrom:str, *pairs:Tuple[str,str]):
        for inp, stateTo in pairs:
            self.transition(stateFrom, inp, stateTo)

    # ignore -- Menandai semua karakter yang diberikan sebagai karakter yang diabaikan
    def ignore(self, chars:str):
        self._ignore = chars

    # start -- Menandai state sebagai starting state
    def start(self, state:str):
        self._start = state

    # accept -- Menandai semua state yang diberikan sebagai accepting state
    def accept(self, *states:str):
        for s in states:
            self.state(s)
            if s not in self._accept: self._accept.append(s)

# TESTING
if __name__ == '__main__':
    alphabet = [chr(c) for c in range(ord('a'), ord('z')+1)]
    alphabet.append([chr(C) for C in range(ord('A'), ord('Z')+1)])
    numeric = [chr(c) for c in range(ord('0'), ord('9')+1)]
    sign = '+-'
    ops = '+-*/'
    blank = ' '

    A = DFA()
    """
    A.start('term')
    A.accept('termlit', 'termnum')
    A.transitions('term', (alphabet, 'termlit'), (numeric, 'termnum'), (sign, 'termsigned'))
    A.transitions('termsigned', (alphabet, 'termlit'), (numeric, 'termnum'))
    A.transitions('termlit', (alphabet, 'termlit'), (numeric, 'termlit'))
    A.transitions('termnum', (numeric, 'termnum'))
    """
    #Arithmetic Operations
    def tesarit():
        A = DFA()
        A.start('A')
        A.accept('B')
        A.transitions('A', (numeric,'B'), (blank,'A'))
        A.transitions('B', (numeric,'B'), (blank,'B'),(ops,'A'))
        print(A._states)
        print(A._accept)
        #print(A._delta)

        print('Input string: ', end='')
        s = str(input())

        print(f'DFA {"accepts" if A.get(s) else "rejects"}')

    #Assignment
    def assignment():
        A = DFA()
        A.start('q0')
        A.accept('q4')
        A.transitions('q0', (alphabet,'q1'))
        A.transitions('q1', (alphabet,'q1'), (numeric,'q1'), (blank,'q2'), ('=','q3'))
        A.transitions('q2', (numeric,'metong'),('=','q3'))
        A.transitions('q3', (blank,'q3'), (numeric,'q4'), (alphabet,'q4'))
        A.transitions('q4', (numeric,'q4'), (alphabet,'q4'), (blank,'q6'), (ops,'q5'))
        A.transitions('q5', (numeric,'q4'), (blank,'q5'))
        A.transitions('q6', (alphabet,'metong'),(ops,'q3'),(numeric,'metong'),(blank,'q6'))
        A.transitions('metong', (alphabet,'metong'),(ops,'metong'),(numeric,'metong'),(blank,'metong'))

        print(A._states)
        print(A._accept)
        #print(A._delta)

        print('Input string: ', end='')
        s = str(input())

        print(f'DFA {"accepts" if A.get(s) else "rejects"}')
    
    #Variable name

    '''
    print(A._states)
    print(A._accept)
    #print(A._delta)

    print('Input string: ', end='')
    s = str(input())

    print(f'DFA {"accepts" if A.get(s) else "rejects"}')
    '''

    tesarit()
    assignment()
