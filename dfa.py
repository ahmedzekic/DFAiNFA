

class DFA:
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
        self.trenutno_stanje = ps
        
    def promijeni_stanje(self, slovo):
        if slovo not in self.alfabet:
            raise NameError("slovo nije u alfabetu")
        self.trenutno_stanje = self.funkcija_tranzicije[(self.trenutno_stanje, slovo)]
        
    def prihvata(self, string):
        for slovo in string:
            self.promijeni_stanje(slovo)
        return self.trenutno_stanje in self.zavrsna_stanja
        
s = {0,1,2,3} #skup stanja
alf = {"a","b"}
z = {2} #zavrsna stanja
ftr = dict() #tabela tranzicija
ftr[(0,"a")] = 0
ftr[(0,"b")] = 1

ftr[(1,"a")] = 0
ftr[(1,"b")] = 2

ftr[(2,"a")] = 3
ftr[(2,"b")] = 0

ftr[(3,"a")] = 3
ftr[(3,"b")] = 1

d = DFA(s,alf,ftr,0,z)
print (d.prihvata("aaaabb"))
