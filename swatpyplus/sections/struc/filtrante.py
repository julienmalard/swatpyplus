from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    code = 'NAME'


class IndicFiltrante(VarRéel):
    nom = "Indicateur bande filtrante"
    code = 'FLAG'


class RatioChampFiltrante(VarRéel):
    nom = "Ratio de la zone de champ sur la zone de la bande filtrante"
    code = 'FLD_VFS'


class FractionFlux(VarRéel):
    nom = "Fraction de flux entrant dans les 10% les plus concentrés du filtre"
    code = 'CON_VFS'


class ConcCanal(VarRéel):
    nom = "Concentration d'écoulement entièrement canalisé"
    code = 'CHA_Q'


vars_ = [Nom, IndicFiltrante, RatioChampFiltrante, FractionFlux, ConcCanal]


class DivisionFiltrante(Division):
    variables = vars_


class Filtrante(Fichier):
    nom = 'filterstrip.str'
    division = DivisionFiltrante
