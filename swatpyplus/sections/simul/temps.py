from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarCatég


class JourInitial(VarEntier):
    nom = 'Jour initial'
    cod = 'DAY_START'


class AnnéeInitiale(VarEntier):
    nom = 'Année initiale'
    cod = 'YEAR_START'


class JourFinal(VarEntier):
    nom = 'Jour final'
    cod = 'DAY_END'


class AnnéeFinale(VarEntier):
    nom = 'Année finale'
    cod = 'YEAR_END'


class Incrément(VarCatég):
    nom = 'Incrément'
    cod = 'STEP'
    valeurs = [0, 1, 24, 96, 1440]


vars_ = [
    JourInitial,
    AnnéeInitiale,
    JourFinal,
    AnnéeFinale,
    Incrément
]


class Temps(Fichier):
    nom = 'time.sim'
    variables = vars_
