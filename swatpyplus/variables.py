class Variable(object):
    nom = ''
    cod = ''
    unité = ''


class VarNumérique(Variable):
    pass


class VarEntier(VarNumérique):
    pass


class VarRéel(VarNumérique):
    pass


class VarCatégo(Variable):
    valeurs = []


class VarTexte(Variable):
    pass


class VarOuiNon(VarCatégo):
    valeurs = ['y', 'n']
