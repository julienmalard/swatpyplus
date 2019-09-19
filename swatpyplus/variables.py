class Variable(object):
    nom = ''
    code = ''
    unité = ''
    dtype = None


class VarNumérique(Variable):
    pass


class VarEntier(VarNumérique):
    dtype = int


class VarRéel(VarNumérique):
    dtype = float


class VarCatégo(Variable):
    valeurs = []
    dtype = str


class VarTexte(Variable):
    dtype = str


class VarOuiNon(VarCatégo):
    valeurs = ['y', 'n']
