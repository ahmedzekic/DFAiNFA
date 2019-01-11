

class DFA:
    def __init__(self, states, alphabet, transition_f, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_f
        if start_state not in states:
            raise NameError("start state is not in set of states")
        self.start_state = start_state
        if not accept_states <= states:
            raise NameError("accept states are not in set of states")
        self.accept_states = accept_states
        self.current_state = start_state
        
    def __str__(self):
        out = (("Set of states: " + str(self.states)) + "\n" + ("Alphabet: " + str(self.alphabet)) + "\n"
        + ("Transition function: " + str(self.transition_function)) + "\n" + ("Start state: " + str(self.start_state)) 
        + "\n" + ("Accept states: " + str(self.accept_states)))
        return out
        
    def __repr__(self):
        return str(self)
        
    def change_state(self, symbol):
        if symbol not in self.alphabet:
            raise NameError("symbol is not in alphabet")
        self.current_state = self.transition_function[(self.current_state, symbol)]
        
    def accepts(self, string):
        for symbol in string:
            self.change_state(symbol)
        return self.current_state in self.accept_states      
"""example"""
        
s = {0,1,2,3} #set of states
alph = {"a","b"}
a = {2} #accept states
ftr = dict() #transition function
ftr[(0,"a")] = 0
ftr[(0,"b")] = 1

ftr[(1,"a")] = 0
ftr[(1,"b")] = 2

ftr[(2,"a")] = 3
ftr[(2,"b")] = 0

ftr[(3,"a")] = 3
ftr[(3,"b")] = 1

d = DFA(s,alph,ftr,0,a)
print (d)
print (d.accepts("aaaabb"))