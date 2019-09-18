from swatpyplus.div import DivisionPartition
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarEntier, VarRéel


class Nom(VarTexte):
    nom = 'Nom de la région'
    cod = 'NAME'


class NombreÉléments(VarEntier):
    nom = "Nombre d'éléments d'utilisation du territoire"
    cod = 'NLUM'


class NumRégion(VarEntier):
    nom = 'Numéro de la région'
    cod = 'NREG'


class NomÉlément(VarEntier):
    nom = "Nom de l'élément d'utilisation du territoire"
    cod = 'NAME'


class ÉcoulementSurface(VarRéel):
    nom = "Ratio d'écoulement de surface"
    cod = 'SRR'


class ÉcoulementLatéral(VarRéel):
    nom = "Ratio d'écoulement latéral"
    cod = 'LFR'


class Percolation(VarRéel):
    nom = "Ratio percolation"
    cod = 'PCR'


class Évapotranspiration(VarRéel):
    nom = "Ratio d'évapotranspiration"
    cod = 'ETR'


class FluxDrains(VarRéel):
    nom = "Ratio de flux par les drains"
    cod = 'TFR'


class Sédiment(VarRéel):
    nom = "Rendement de sédiment"
    cod = 'SED'


class NOrganique(VarRéel):
    nom = "Rendement de N organique"
    cod = 'ORGN'


class POrganique(VarRéel):
    nom = "Rendement de P organique"
    cod = 'ORGP'


class NO3(VarRéel):
    nom = "Rendement de NO3"
    cod = 'NO3'


class PSoluble(VarRéel):
    nom = "Rendement de P soluble"
    cod = 'SOLP'


vars_entête = [
    Nom, NombreÉléments, NumRégion
]

vars_secondaires = [
    NomÉlément, ÉcoulementSurface, ÉcoulementLatéral, Percolation, Évapotranspiration, FluxDrains, Sédiment,
    NOrganique, POrganique, NO3, PSoluble
]


class DivisionUtilTerr(DivisionPartition):
    vars_entête = vars_entête
    vars_secondaires = vars_secondaires
    var_n_lignes = NombreÉléments


class UtilisationTerritoire(Fichier):
    nom = 'ls_regions.cal'
    variables = [*vars_secondaires, *vars_entête]
    division = DivisionUtilTerr
