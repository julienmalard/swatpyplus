from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarCatégo


class JourInitial(VarEntier):
    nom = 'Jour initial'
    code = 'DAY_START'


class AnnéeInitiale(VarEntier):
    nom = 'Année initiale'
    code = 'YRC_START'


class JourFinal(VarEntier):
    nom = 'Jour final'
    code = 'DAY_END'


class AnnéeFinale(VarEntier):
    nom = 'Année finale'
    code = 'YRC_END'


class Incrément(VarCatégo):
    nom = 'Incrément'
    code = 'STEP'
    valeurs = [0, 1, 24, 96, 1440]


vars_ = [
    JourInitial,
    AnnéeInitiale,
    JourFinal,
    AnnéeFinale,
    Incrément
]


class DivisionTemps(Division):
    variables = vars_


class Temps(Fichier):
    nom = 'time.sim'
    division = DivisionTemps
