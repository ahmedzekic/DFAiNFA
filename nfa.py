from itertools import combinations

class NFA:
    def __init__(self, stanja, alfabet, fja_tranzicije, ps, zs):
        self.stanja = stanja
        self.alfabet = alfabet
        self.funkcija_tranzicije = fja_tranzicije
        if ps not in stanja:
            raise NameError("pocetno stanje nije u skupu stanja")
        self.pocetno_stanje = ps
        if not zs <= stanja:
            raise NameError("zavrsna stanja nisu u skupu stanja")
        self.zavrsna_stanja = zs
        self.trenutna_stanja = {ps}
        
    def promijeni_stanje(self, slovo):
        if slovo not in self.alfabet:
            raise NameError("slovo nije u alfabetu")
        pom = set()
        for i in self.trenutna_stanja:
            if (i, slovo) in self.funkcija_tranzicije:
                pom = pom | self.funkcija_tranzicije[(i, slovo)]
        self.trenutna_stanja = pom
       
        
    def provjeri_epsilon_grane(self, stanja): #dodat argument pa da radi i za pretvori u dfa
        pom_lista = list(stanja)
        for stanje in pom_lista:
                if (stanje, "epsilon") in self.funkcija_tranzicije:
                    pom_lista += self.funkcija_tranzicije[(stanje, "epsilon")]
        return set(pom_lista)
                
        
    def prihvata(self, string):
        self.trenutna_stanja = self.provjeri_epsilon_grane(self.trenutna_stanja)
        print (self.trenutna_stanja)
        for slovo in string:
            self.promijeni_stanje(slovo)
            self.trenutna_stanja = self.provjeri_epsilon_grane(self.trenutna_stanja)
            print (self.trenutna_stanja)
            if len(self.trenutna_stanja) == 0:
                return False
        if self.trenutna_stanja & self.zavrsna_stanja:
                return True
        return False
        
    def pretvori_u_DFA(self):
        stanja_dfa = set()
        for i in range(len(self.stanja)+1):
            stanja_dfa = stanja_dfa | set(combinations(self.stanja, i))
        print (stanja_dfa)
        ftr_dfa = dict()
        for slovo in self.alfabet:
            for stanje in stanja_dfa:
                pom = set()
                for i in range(len(stanje)):
                    if (stanje[i],slovo) in self.funkcija_tranzicije:
                        pom = pom | self.funkcija_tranzicije[(stanje[i],slovo)]
                        pom = self.provjeri_epsilon_grane(pom)
                ftr_dfa[(stanje,slovo)] = pom
        for stanje in stanja_dfa:
            if set(stanje) not in ftr_dfa.values():
                for slovo in self.alfabet:
                    del ftr_dfa[(stanje,slovo)]
        print (ftr_dfa)
        
        
s = {0,1,2,3} #skup stanja
alf = {"a","b"}
z = {2} #zavrsna stanja
ftr = dict() #tabela tranzicija
ftr[(0,"a")] = {0}
ftr[(0,"b")] = {1}
ftr[(0,"epsilon")] = {2}

ftr[(1,"a")] = {0}
ftr[(1,"b")] = {2,3}

#ftr[(2,"a")] = set()
ftr[(2,"b")] = {0,2}
ftr[(2,"epsilon")] = {3}



ftr[(3,"a")] = {3}
ftr[(3,"b")] = {1}

ftr2 = dict()
ftr2[(1,'b')] = {2}
ftr2[(1,'epsilon')] = {3}
#ftr2[(1,'a')] = set()

ftr2[(2,'a')] = {2,3}
ftr2[(2,'b')] = {3}

ftr2[(3,'a')] = {1}
#ftr2[(3,'b')] = set()

m = NFA({1,2,3},alf,ftr2,1,{1})
print (m.prihvata("aaaababba"))
m.pretvori_u_DFA()

n = NFA(s,alf,ftr,0,z)
#n.pretvori_u_DFA()
print (n.prihvata("aaaababba"))

test = dict()
test[(1,'a')] = {2}
test[(1,'b')] = set()
test[(2,'b')] = {2}
test[(2,'epsilon')] = {1}
testnfa = NFA({1,2},alf,test,1,{1})
#print (testnfa.prihvata('ab'))

