class VariableMap(object):
    """ Mapovanie mien premennych na cisla.

    Premennym vzdy priraduje suvisly usek cisel 1..n.
    """
    def __init__(self, variables = []):
        """ Vytvori nove mapovanie, ktore bude obsahovat premenne z variables. """
        self.max = 0
        self.map = {}
        for var in variables:
            self.addVar(var)

    def addVar(self, var):
        """ Prida premennu var.

        Ak je uz v mape, nic sa nestane, ak nie prida ju s dalsim cislom v poradi.
        Vrati referenciu na seba, aby sa dala zretazovat.
        """
        if var not in self.map:
            self.max += 1
            self.map[var] = self.max
        return self

    def get(self, var):
        """ Vrati cislo priradene premennej var.

        Vyhodi KeyError vynimku ak taka premenna nie je v mape.
        """
        return self.map[var] # throws KeyError, which is OK

    def __getitem__(self, var):
        """ Vrati cislo priradene premennej var.

        Vyhodi KeyError vynimku ak taka premenna nie je v mape.
        """
        return self.get(var)

    def keys(self):
        """ Vrati zoznam vsetkych premennych v mape. """
        return self.map.keys()

    def toString(self):
        """ Vrati textovu reprezentaciu mapovania premennych.

        Napriklad vo formate "{'a':1, 'b':2, ...}" alebo podobnom.
        """
        return repr(self.map)

    def reverse(self):
        """ Vrati reverzne mapovanie ako jednoduchy slovnik z cisel na mena premennych. """
        rev = {}
        for k,v in self.map.items():
            rev[v] = k
        return rev

    def writeToFile(self, outFile):
        """ Zapise mapu do suboru outFile. """
        outFile.write('%d\n' % self.max)
        rev = self.reverse()
        for i in range(self.max):
            outFile.write('%s\n' % rev[i+1])

    @staticmethod
    def readFromFile(inFile):
        """ Nacita novu mapu zo suboru inFile a vrati ju. """
        varMap = VariableMap([])
        n = int(inFile.readline())
        for i in range(n):
            varMap.addVar(inFile.readline().strip())
        return varMap



class CnfLit(object):
    """ Reprezentacia literalu (premenna alebo negovana premenna) v CNF formule. """
    def __init__(self, name):
        """ Vytvori novy, kladny (nenegovany) literal pre premennu name. """
        self.name = name
        self.neg = False

    @staticmethod
    def Not(name):
        """ Vytvory novy, negovany literal pre premennu name. """
        v = CnfLit(name)
        v.neg = True
        return v

    def __neg__(self):
        """ Vrati novy literal, ktory je negaciou tohoto. """
        lit = CnfLit(self.name)
        lit.neg = not self.neg
        return lit

    def toString(self):
        """ Vrati textovu reprezentaciu tohoto literalu (vid zadanie). """
        if self.neg:
            return "-" + self.name
        else:
            return self.name

    def eval(self, i):
        """ Vrati ohodnotenie tohoto literalu pri interpretacii i. """
        return bool(self.neg) ^ bool(i[self.name])

    def extendVarMap(self, varMap):
        """ Rozsiri varMap o premennu v tomto literali. """
        varMap.addVar(self.name)

    def writeToFile(self, outFile, varMap):
        """ Zapise literal do suboru outFile s pouzitim mapovania premennych varMap. """
        if self.neg:
            outFile.write('-%d' % varMap[self.name])
        else:
            outFile.write('%d' % varMap[self.name])

class CnfClause(list):
    """ Reprezentacia klauzy (pole literalov). """
    def __init__(self, vars = []):
        """ Vytvori novu klauzu obsahujucu literaly literals. """
        list.__init__(self, vars)

    def toString(self):
        """ Vrati textovu reprezentaciu tejto klauzy (vid zadanie). """
        return ' '.join([var.toString() for var in self])

    def eval(self, i):
        """ Vrati ohodnotenie tejto klauzy pri interpretacii i. """
        for var in self:
            if var.eval(i):
                return True
        return False

    def extendVarMap(self, varMap):
        """ Rozsiri varMap o premenne v tejto klauze. """
        for lit in self:
            lit.extendVarMap(varMap)

    def writeToFile(self, oFile, varMap):
        """ Zapise klauzu do suboru outFile v DIMACS formate
            pricom pouzije varMap na zakodovanie premennych na cisla.

        Klauzu zapise na jeden riadok (ukonceny znakom konca riadku).
        """
        for var in self:
            var.writeToFile(oFile, varMap)
            oFile.write(' ')
        oFile.write(' 0\n')

    @staticmethod
    def readFromFile(inFile, varMap):
        """ Nacita novu klauzu zo suboru inFile a vrati ju ako vysledok.

        Mozete predpokladat, ze klauza je samostatne na jednom riadku.

        Ak sa z aktualneho riadku na vstupe neda nacitat korektna klauza,
        vyhodi vynimku IOError.
        """
        line = inFile.readline()
        if line is None:
            raise IOError('End of file')

        rVarMap = varMap.reverse()

        cls = CnfClause([])
        ints = [int(x) for x in line.split()]
        if len(ints) < 1 or ints[-1] != 0:
            raise IOError('Bad clause')
        for i in ints[:-1]:
            if i < 0:
                cls.append(CnfLit.Not(rVarMap[abs(i)]))
            else:
                cls.append(CnfLit(rVarMap[abs(i)]))
        return cls

class Cnf(list):
    """ Reprezentacia Cnf formuly ako pola klauz. """
    def __init__(self, clauses = []):
        """ Vytvori novu Cnf formuly obsahujucu klauzy clauses. """
        list.__init__(self, clauses)

    def toString(self):
        """ Vrati textovu reprezentaciu tejto formule (vid zadanie). """
        return ''.join([ cls.toString() + '\n' for cls in self])

    def eval(self, i):
        """ Vrati ohodnotenie tejto formule pri interpretacii i. """
        for cls in self:
            if not cls.eval(i):
                return False
        return True

    def extendVarMap(self, varMap):
        """ Rozsiri varMap o premenne v tejto formule. """
        for cls in self:
            cls.extendVarMap(varMap)

    def writeToFile(self, oFile, varMap):
        """ Zapise klauzu do suboru outFile v DIMACS formate
            pricom pouzije varMap na zakodovanie premennych na cisla a
            zapise kazdu klauzu na jeden riadok.
        """
        for cls in self:
            cls.writeToFile(oFile, varMap)

    @staticmethod
    def readFromFile(inFile, varMap):
        """ Nacita novu formulu zo suboru inFile a vrati ju ako vysledok.

        Mozete predpokladat, ze kazda klauza je samostatne na jednom riadku.
        """
        cnf = Cnf([])
        while True:
            try:
                cls = CnfClause.readFromFile(inFile, varMap)
            except IOError:
                break
            cnf.append(cls)
        return cnf

# vim: set sw=4 ts=4 sts=4 et :
