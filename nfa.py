from itertools import combinations
from dfa import DFA

class NFA:
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
        self.current_states = {start_state}
        
    def __str__(self):
        out = (("Set of states: " + str(self.states)) + "\n" + ("Alphabet: " + str(self.alphabet)) + "\n"
        + ("Transition function: " + str(self.transition_function)) + "\n" + ("Start state: " + str(self.start_state)) 
        + "\n" + ("Accept states: " + str(self.accept_states)))
        return out
        
    def __repr__(self):
        return str(self)
        
    def change_states(self, symbol):
        if symbol not in self.alphabet:
            raise NameError("symbol is not in alphabet")
        temp = set()
        for i in self.current_states:
            if (i, symbol) in self.transition_function:
                temp = temp | self.transition_function[(i, symbol)]
        self.current_states = temp
       
        
    def check_epsilon_branches(self, states):
        temp_list = list(states)
        for state in temp_list:
                if (state, "epsilon") in self.transition_function:
                    temp_list += self.transition_function[(state, "epsilon")]
        return set(temp_list)
                
        
    def accepts(self, string):
        self.current_states = self.check_epsilon_branches (self.current_states)
        for symbol in string:
            self.change_states(symbol)
            self.current_states = self.check_epsilon_branches(self.current_states)
            if len(self.current_states) == 0:
                return False
        if self.current_states & self.accept_states:
                return True
        return False
        
    def convert_to_DFA(self):
        states_DFA = set()
        for i in range(len(self.states)+1):
            states_DFA = states_DFA | set(combinations(self.states, i))
        ftr_dfa = dict()
        for symbol in self.alphabet:
            for state in states_DFA:
                temp = set()
                for i in range(len(state)):
                    if (state[i],symbol) in self.transition_function:
                        temp = temp | self.transition_function[(state[i],symbol)]
                        temp = self.check_epsilon_branches(temp)
                ftr_dfa[(state,symbol)] = tuple(temp)
        start_state_DFA = self.check_epsilon_branches({self.start_state})
        start_state_DFA = tuple(start_state_DFA)
        surplus_states = set()
        for state in states_DFA:
            if state not in ftr_dfa.values() and state != start_state_DFA:
                surplus_states.add(state)
                for symbol in self.alphabet:
                    del ftr_dfa[(state,symbol)]
        states_DFA = states_DFA - surplus_states
        accept_states_DFA = set()
        for accept_state_NFA in self.accept_states:
            for state_DFA in states_DFA:
                for i in state_DFA:
                    if  i == accept_state_NFA:
                        accept_states_DFA.add(state_DFA)
        return DFA(states_DFA, self.alphabet, ftr_dfa, start_state_DFA, accept_states_DFA)
            
"""example"""   

#----------------------------------------example no 1--------------------------------------------
"""
s = {0,1,2,3} #set of states
alf = {'a','b'} #alphabet
z = {2} #accept states

ftr = dict() #tabela tranzicija
ftr[(0,"a")] = {0}
ftr[(0,"b")] = {1}
ftr[(0,"epsilon")] = {2}

ftr[(1,"a")] = {0}
ftr[(1,"b")] = {2,3}

ftr[(2,"b")] = {0,2}
ftr[(2,"epsilon")] = {3}

ftr[(3,"a")] = {3}
ftr[(3,"b")] = {1}


nfa_test = NFA({0,1,2,3},alf,ftr,1,{1})
print (nfa_test)
print (nfa_test.accepts("aaaababb"))
dfa_test = nfa_test.convert_to_DFA()
print(dfa_test)
print (dfa_test.accepts("aaaababb"))"""

#-----------------------------------------example no 2--------------------------------------

ftr2 = dict()
ftr2[(1,'b')] = {2}
ftr2[(1,'epsilon')] = {3}

ftr2[(2,'a')] = {2,3}
ftr2[(2,'b')] = {3}

ftr2[(3,'a')] = {1}

n = NFA({1,2,3},alf,ftr2,1,{1})
print (n)
print (n.accepts("aaaababba"))
d = n.convert_to_DFA()
print(d)
print (d.accepts("aaaababba"))


#--------------------------------------------example no 3---------------------------------------------
"""
ah = dict()
ah[(0,"a")] = {1}
ah[(0,"epsilon")] = {2}
ah[(2,"a")] = {2}

t = NFA({0,1,2},{"a"},ah,0,{2})
print(t)
print(t.accepts("a"))
D = t.convert_to_DFA()
print(D)
print(D.accepts("a"))"""


