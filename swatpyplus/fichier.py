class Fichier(object):
    nom = ''
    variables = []
    var_lignes_division = None


class FichierDivisions(Fichier):
    vars_entête = []
    vars_soussection = []


class FichierDivisionsAlignées(FichierDivisions):
    pass
