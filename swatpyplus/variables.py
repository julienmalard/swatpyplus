class Variable(object):
    nom = ''
    cod = ''
    unité = ''

    def __init__(soimême, val):
        soimême.val = val


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
