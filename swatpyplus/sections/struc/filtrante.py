from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    cod = 'NAME'


class IndicFiltrante(VarRéel):
    nom = "Indicateur bande filtrante"
    cod = 'FLAG'


class RatioChampFiltrante(VarRéel):
    nom = "Ratio de la zone de champ sur la zone de la bande filtrante"
    cod = 'FLD_VFS'


class FractionFlux(VarRéel):
    nom = "Fraction de flux entrant dans les 10% les plus concentrés du filtre"
    cod = 'CON_VFS'


class ConcCanal(VarRéel):
    nom = "Concentration d'écoulement entièrement canalisé"
    cod = 'CHA_Q'


vars_ = [Nom, IndicFiltrante, RatioChampFiltrante, FractionFlux, ConcCanal]


class Filtrante(Fichier):
    nom = 'filterstrip.str'
    variables = vars_
