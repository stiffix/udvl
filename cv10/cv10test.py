#! /bin/env python3
#
# Testovaci program pre ham kniznicu
#
# Kniznica musi byt v subore ham.py a musi implementovat triedu
# HamiltonianCycle s metodou find.
#

import sys
import time
import traceback

from ham import HamiltonianCycle

""" Nastavte na True ak chcete aby testy zastali na prvej chybe. """
stopOnError = False

class FailedTestException(BaseException):
    pass

def now():
    try:
       return time.perf_counter() # >=3.3
    except AttributeError:
       return time.time() # this is not monotonic!

def printException():
    print('ERROR: Exception raised:\n%s\n%s\n%s' % (
        '-'*20,
        traceback.format_exc(),
        '-'*20)
    )

class Tester(object):
    def __init__(self):
        self.case = 0
        self.tested = 0
        self.passed = 0

    def fail(self, msg):
        print('ERROR: %s' % msg)
        return False;

    def checkGood(self, m, r):
        if len(m) != len(r):
            return self.fail('Wrong result length!')
        last = r[-1]
        for v in r:
            if not m[last][v]:
                return self.fail('No edge %d -> %d' % (last, v))
            last = v
        return True

    def checkBad(self, r):
        if len(r) != 0:
            return self.fail('non-empty result when there should be no cycle')
        return True

    def check(self, m, good, r):
        if good:
            return self.checkGood(m, r)
        else:
            return self.checkBad(r)


    def test(self, m, good):
        self.case += 1
        self.tested += 1
        sys.stdout.write('Case %d:  ' % (self.case,))

        try:
            start = now()
            r = HamiltonianCycle().find(m)
            duration = now() - start
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            printException()
            if stopOnError:
                raise FailedTestException()
            return


        if self.check(m, good, r):
            self.passed += 1
            print('PASSED  duration %s' % duration)
        else:
            print('edges:')
            for row in m:
                print(' '.join(('1' if x else '0') for x in row))
            print('')
            print('result: %s' % repr(r))
            print('')
            if stopOnError:
                raise FailedTestException()

    def status(self):
        print("self.tested %d" % (self.tested,))
        print("self.passed %d" % (self.passed,))
        if self.tested == self.passed:
            print("OK")
        else:
            print("ERROR")


def edgesToIncidenceMatrix(edges):
    a, b = zip(*edges)
    n = max(a+b)+1

    m = []
    for row in range(n):
        m.append([False] * n)
    for a,b in edges:
        m[a][b] = True
    return m


t = Tester()
try:

    m = [
            [True, True],
            [True, True]
        ]
    t.test(m, True)

    m = [
            [False, True],
            [False, False],
        ]
    t.test(m, False)

    m = edgesToIncidenceMatrix([
            (0, 3),
            (0, 4),
            (1, 0),
            (1, 3),
            (1, 4),
            (2, 1),
            (2, 5),
            (3, 0),
            (3, 4),
            (4, 1),
            (4, 2),
            (4, 5),
            (5, 2),
            (5, 4),
        ])

    t.test(m, True)


    print("END")

except FailedTestException:
    print("Stopped on first failed test!")
finally:
    t.status()

# vim: set sw=4 ts=4 sts=4 et :
