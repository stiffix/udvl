import tableau

class TableauBuilder(object):
    def build(self, signedFormulas):
        """ Vytvori a vrati uzavrete alebo uplne tablo pre zoznam oznacenych formul. """

        # aby sa vrcholy cislovali od 1
        tableau.Node.resetLastNumber()

        # vyplnime prve vrcholy podla zoznamu vstupnych formul
        tabl = None
        leaf = None
        for sign, formula in signedFormulas:
            newNode = tableau.Node(sign, formula)
            if leaf is None:
                tabl = newNode
            else:
                leaf.children.append(newNode)
            leaf = newNode

        # TODO vytvorit tablo

        return tabl

# vim: set sw=4 ts=8 sts=4 et :
