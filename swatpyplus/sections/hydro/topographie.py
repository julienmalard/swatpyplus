from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarRéel, VarTexte


class Nom(VarTexte):
    nom = 'Nom'
    code = 'name'


class PenteURH(VarRéel):
    nom = 'Pente moyenne en URH'
    code = 'SLP'
    unité = 'm/m'


class LongeurPente(VarRéel):
    nom = 'Longueur moyenne de la pente en URH'
    code = 'SLP_LEN'
    unité = 'm'


class LongeurSouterrain(VarRéel):
    nom = "Longueur de la pente pour l'écoulement souterrain latéral"
    code = 'LAT_LEN'
    unité = 'm'


class DistFlux(VarRéel):
    nom = "Distance moyenne au flux"
    code = 'DIST_CHA'
    unité = 'm'


class CoeffDep(VarRéel):
    nom = "Coefficient de depot"
    code = 'DEPOS'


vars_ = [Nom, PenteURH, LongeurPente, LongeurSouterrain, DistFlux, CoeffDep]


class DivisionTopographie(Division):
    variables = vars_


class Topographie(Fichier):
    nom = 'Topography.hyd'
    division = DivisionTopographie
