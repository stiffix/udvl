import cnf

class Formula(object):
    def __init__(self, subs = []):
        self.m_subf = subs
    def subf(self):
        return self.m_subf
    def eval(self, i):
        return False
    def toString(self):
        return "INVALID"
    def toCnf(self):
        """ Vrati reprezentaciu formuly v CNF tvare. """
        return cnf.Cnf()

class Variable(Formula):
    def __init__(self, name):
        Formula.__init__(self)
        self.name = name
    def eval(self, i):
        return i[self.name]
    def toString(self):
        return self.name

class Negation(Formula):
    def __init__(self, orig):
        Formula.__init__(self, [orig])
    def originalFormula(self):
        return self.subf()[0]
    def eval(self, i):
        return not self.originalFormula().eval(i)
    def toString(self):
        return "-%s" % (self.originalFormula().toString())

class Disjunction(Formula):
    def __init__(self, subs):
        Formula.__init__(self, subs)
    def eval(self, i):
        for f in self.subf():
            if f.eval(i):
                return True
        return False
    def toString(self):
        return '(' + '|'.join([f.toString() for f in self.subf()]) + ')'

class Conjunction(Formula):
    def __init__(self, subs):
        Formula.__init__(self, subs)
    def eval(self, i):
        for f in self.subf():
            if not f.eval(i):
                return False
        return True
    def toString(self):
        return '(' + '&'.join([f.toString() for f in self.subf()]) + ')'



class Binary(Formula):
    def __init__(self, left, right, conj):
        Formula.__init__(self, [left, right])
        self.conj = conj
    def left(self):
        return self.subf()[0]
    def right(self):
        return self.subf()[1]
    def toString(self):
        return '(%s%s%s)' % (self.left().toString(), self.conj, self.right().toString())

class Implication(Binary):
    def __init__(self, left, right):
        Binary.__init__(self, left, right, '=>')
    def eval(self, i):
        return (not self.left().eval(i)) or self.right().eval(i)

class Equivalence(Binary):
    def __init__(self, left, right):
        Binary.__init__(self, left, right, '<=>')
    def eval(self, i):
        return self.left().eval(i) == self.right().eval(i)

# vim: set sw=4 ts=4 sts=4 et :
