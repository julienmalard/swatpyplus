from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarRéel, VarTexte


class Nom(VarTexte):
    nom = 'Nom'
    cod = 'name'


class PenteURH(VarRéel):
    nom = 'Pente moyenne en URH'
    cod = 'SLP'
    unité = 'm/m'


class LongeurPente(VarRéel):
    nom = 'Longueur moyenne de la pente en URH'
    cod = 'SLP_LEN'
    unité = 'm'


class LongeurSouterrain(VarRéel):
    nom = "Longueur de la pente pour l'écoulement souterrain latéral"
    cod = 'LAT_LEN'
    unité = 'm'


class DistFlux(VarRéel):
    nom = "Distance moyenne au flux"
    cod = 'DIST_CHA'
    unité = 'm'


class CoeffDep(VarRéel):
    nom = "Coefficient de depot"
    cod = 'DEPOS'


vars_ = [Nom, PenteURH, LongeurPente, LongeurSouterrain, DistFlux, CoeffDep]


class Topographie(Fichier):
    nom = 'Topography.hyd'
    variables = vars_
