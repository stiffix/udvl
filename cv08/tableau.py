ALPHA = 1
BETA  = 2

def signedFormToString(sf):
    formula, sign = sf
    return '{} {}'.format('T' if sign else 'F', formula.toString())

class Node(object):
    
    def __init__(self, sign, formula, source = None):
        self.formula = formula
        self.sign = sign
        self.number = self._nextNumber()
        self.source = source
        self.closed = False
        self.children = []
    
    _lastNumber = 0
        
    @classmethod
    def resetLastNumber(self, newNumber = 0):
        self._lastNumber = newNumber
    
    @classmethod
    def numberOfNodes(self):
        return self._lastNumber
    
    @classmethod
    def _nextNumber(self):
        self._lastNumber += 1
        return self._lastNumber
    
    def isClosed(self):
        if self.children:
            self.closed = all([ child.isClosed() for child in self.children ])
            return self.closed
        else:
            return self.closed
    
    def toString(self):
        return '\n'.join( self._lines() )
    
    _separator = ' | '
    
    def label(self):
        nsf = '({}) {}'.format(self.number,
                               signedFormToString((self.formula, self.sign)))
        if self.source != None:
            return '{} ({})'.format(nsf, self.source.number)
        else:
            return nsf

    def _width(self):
        form_wd = len( self.label() )
        children_wd = sum( [ child._width() for child in self.children ] )
        children_wd += len(self._separator) * max(0, len(self.children) - 1)
        return max(form_wd, children_wd)
    
    def _lines(self):
        width = self._width()

        lines = [ self.label() ]
        if self.children:
            if len(self.children) > 1:
                lines.append('-' * width)
            lines.extend( self._mergeChildLines() )
        elif self.closed:
            lines.append( '*' )

        return [ line.center(width) for line in lines ]

    def _mergeChildLines(self):
        chLines  = [ child._lines() for child in self.children ]
        ch_widths = [ child._width() for child in self.children ]
        ch_len = len(self.children)
        lines = []
        allEmpty = False

        while not allEmpty:
            allEmpty = True
            lineParts = []
            for i in range(ch_len):
                if len(chLines[i]) > 0:
                    # use an i-th child line and remove it from the list
                    chLine = chLines[i].pop(0)
                    lineParts.append( chLine )
                    allEmpty = False
                else:
                    # i-th child has no more lines, pad with spaces
                    lineParts.append( ' ' * ch_widths[i] )
            if not allEmpty:
                lines.append( self._separator.join(lineParts) )
        return lines

# vim: set sw=4 ts=8 sts=4 et :
