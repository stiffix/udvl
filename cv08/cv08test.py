#!/bin/env python3

import traceback
import time
import itertools

"""
    Testovaci program pre TableauBuilder
"""


""" Nastavte na True ak chcete aby testy zastali na prvej chybe. """
stopOnError = False

from builder import TableauBuilder
from tableau import Node, signedFormToString
from formula import Formula, Variable, Negation, Conjunction, Disjunction, Implication, Equivalence

def printException():
    print('ERROR: Exception raised in toCnf:\n%s\n%s\n%s' % (
        '-'*20,
        traceback.format_exc(),
        '-'*20)
    )

def now():
    try:
       return time.perf_counter() # >=3.3
    except AttributeError:
       return time.time() # this is not monotonic!

class FailedTestException(BaseException):
    pass

class Tester(object):
    def __init__(self):
        self.tested = 0
        self.passed = 0
        self.case = 0
        self.closed = 0
        self.size = 0
        self.time = 0

    def compare(self, result, expected, msg):
        self.tested += 1
        if result == expected:
            self.passed += 1
            return True
        else:
            print("Failed: %s:" %  msg)
            print("    got %s  expected %s" % (repr(result), repr(expected)))
            print("")
            return False

    def status(self):
        print("TESTED %d" % (self.tested,))
        print("PASSED %d" % (self.passed,))
        print("SUM(closed) %d" % (self.closed,))
        print("SUM(time) %f" % (self.time,))
        print("SUM(size) %d" % (self.size,))
        if self.tested == self.passed:
            print("OK")
        else:
            print("ERROR")
    
    def closed_open(self, closed):
        return "CLOSED" if closed else "OPEN"

    def testTableau(self, expect_closed, sfs):
        self.case += 1
        self.tested += 1
        print("CASE %d: %s" %
                (self.case,
                 '; '.join([signedFormToString(sf) for sf in sfs ])))
        tableau = Node(Variable(""), False)
        try:
            start = now()
            tableau = TableauBuilder().build(sfs)
            duration = now() - start
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            printException()
            if stopOnError:
                raise FailedTestException()
            return

        if not isinstance(tableau, Node):
            print('FAILED: not a tableau.Node: %s' % type(tableau))
            print()
            return

        closed = tableau.isClosed()
        size = tableau.numberOfNodes()

        self.time += duration
        self.size += size

        if closed:
            self.closed += 1

        if closed == expect_closed:
            self.passed += 1
            print('PASSED:  time: %12.9f   tableau size: %3d   %s' %
                    (duration, size, self.closed_open(closed)))
        else:
            print('FAILED: \n=====TABLEAU=====\n%s\n%s\nTableau is %s, but should be %s' %
                    (tableau.toString(), '='*13,
                     self.closed_open(closed), self.closed_open(expect_closed)))
            if stopOnError:
                raise FailedTestException()
        print('')


t = Tester()

Not = Negation
Var = Variable
Impl = Implication

CLOSED = True
OPEN = False

def And(*args):
    if len(args)==1 and type(args[0]) is list:
        return Conjunction(args[0])
    return Conjunction(args)
def Or(*args):
    if len(args)==1 and type(args[0]) is list:
        return Disjunction(args[0])
    return Disjunction(args)

a = Var('a')
b = Var('b')
c = Var('c')
d = Var('d')


try:
    ### TODO: detailne testy
    
    demorgan1 = Equivalence( Not( And([ a, b ]) ), Or([ Not(a), Not(b) ]) )
    t.testTableau(True, [ (demorgan1, False) ])
    
    demorgan2 = Equivalence( Not( Or([ a, b ]) ), And([ Not(a), Not(b) ]) )
    t.testTableau(True, [ (demorgan2, False) ])
    
    demorgan3 = Equivalence( Not( Or([ a, b, c ]) ),
                             And([ Not(a), Not(b), Not(c) ]) )
    t.testTableau(True, [ (demorgan3, False) ])
    
    contraposition = Equivalence( Impl(a, b), Impl( Not(b), Not(a) ) )
    t.testTableau(True, [ (contraposition, False) ])
    
    impl_impl_distrib = Impl( Impl(a, Impl(b, c)),
                              Impl( Impl(a, b), Impl(a, c) ) )
    t.testTableau(True, [ (impl_impl_distrib, False) ])
    
    impl_or = Equivalence( Impl(a, b), Or([ Not(a), b ]) )
    t.testTableau(True, [ (impl_or, False) ])
    
    impl_and = Equivalence( Impl(a, b), Not( And([ a, Not(b) ]) ) )
    t.testTableau(True, [ (impl_and, False) ])
    
    or_and_distrib = Equivalence( Or([ a, And([ b, c ]) ]),
                                  And([ Or([ a, b ]), Or([ a, c ]) ]) )
    t.testTableau(True, [ (or_and_distrib, False) ])
    
    bad_demorgan1 = Equivalence( Not( And([ a, b ]) ), Or([ a, b ]) )
    t.testTableau(False, [ (bad_demorgan1, False) ])
    
    bad_demorgan2 = Equivalence( Not( Or([ a, b ]) ), Or([ Not(a), Not(b) ]) )
    t.testTableau(False, [ (bad_demorgan2, False) ])
    
    bad_demorgan3 = Equivalence( Not( Or([ a, b, c ]) ),
                             And([ Not(a), b, Not(c) ]) )
    t.testTableau(False, [ (bad_demorgan3, False) ])
    
    bad_contraposition = Equivalence( Impl(a, b), Impl( b, a ) )
    t.testTableau(False, [ (bad_contraposition, False) ])
    
    bad_impl_impl_distrib = Impl( Impl(a, Impl(b, c)),
                              Impl( Impl(b, a), Impl(c, a) ) )
    t.testTableau(False, [ (bad_impl_impl_distrib, False) ])
    
    bad_impl_and = Equivalence( Impl(a, b), Not( And([ Not(a), b ]) ) )
    t.testTableau(False, [ (bad_impl_and, False) ])
    
    bad_or_and_distrib = Equivalence( Or([ a, And([ b, c ]) ]),
                                  Or([ And([ a, b ]), And([ a, c ]) ]) )
    t.testTableau(False, [ (bad_or_and_distrib, False) ])

    ax1 = Implication(Var('dazdnik'), Not(Var('prsi')))
    ax2 = Implication(
                    Var('mokraCesta'),
                    Or( [ Var('prsi'), Var('umyvacieAuto') ] ),
                )
    ax3 = Implication(Var('umyvacieAuto'), Not(Var('vikend')))
    cax1 = Conjunction([ ax1, ax2, ax3 ])
    conclusion = Implication(
                    And( [ Var('dazdnik'), Var('mokraCesta') ] ),
                    Not(Var('vikend')),
                )
    t.testTableau(True, [ (Conjunction([cax1, Not(conclusion)]), True) ])
    t.testTableau(True, [ (Implication(cax1, conclusion), False) ])
    t.testTableau(True, [ (cax1, True), (conclusion, False) ])
    t.testTableau(True, [ (ax1, True), (ax2, True), (ax3, True), (conclusion, False) ])
    t.testTableau(False, [ (cax1, True) ])
    t.testTableau(False, [ (conclusion, False) ])
    
    print("END")

except FailedTestException:
    print("Stopped on first failed test!")
finally:
    t.status()

# vim: set sw=4 ts=4 sts=4 et :
