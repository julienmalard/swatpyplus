from swatpyplus.div import DivisionPartition
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarEntier, VarRéel


class Nom(VarTexte):
    nom = 'Nom de la région'
    code = 'NAME'


class NombreÉléments(VarEntier):
    nom = "Nombre d'éléments d'utilisation du territoire"
    code = 'NLUM'


class NumRégion(VarEntier):
    nom = 'Numéro de la région'
    code = 'NREG'


class NomÉlément(VarTexte):
    nom = "Nom de l'élément d'utilisation du territoire"
    code = 'NAME'


class ÉcoulementSurface(VarRéel):
    nom = "Ratio d'écoulement de surface"
    code = 'SRR'


class ÉcoulementLatéral(VarRéel):
    nom = "Ratio d'écoulement latéral"
    code = 'LFR'


class Percolation(VarRéel):
    nom = "Ratio percolation"
    code = 'PCR'


class Évapotranspiration(VarRéel):
    nom = "Ratio d'évapotranspiration"
    code = 'ETR'


class FluxDrains(VarRéel):
    nom = "Ratio de flux par les drains"
    code = 'TFR'


class Sédiment(VarRéel):
    nom = "Rendement de sédiment"
    code = 'SED'


class NOrganique(VarRéel):
    nom = "Rendement de N organique"
    code = 'ORGN'


class POrganique(VarRéel):
    nom = "Rendement de P organique"
    code = 'ORGP'


class NO3(VarRéel):
    nom = "Rendement de NO3"
    code = 'NO3'


class PSoluble(VarRéel):
    nom = "Rendement de P soluble"
    code = 'SOLP'


vars_entête = [
    Nom, NombreÉléments, NumRégion
]

vars_données = [
    NomÉlément, ÉcoulementSurface, ÉcoulementLatéral, Percolation, Évapotranspiration, FluxDrains, Sédiment,
    NOrganique, POrganique, NO3, PSoluble
]


class DivisionUtilTerr(DivisionPartition):
    vars_entête = vars_entête
    vars_données = vars_données
    var_n_lignes = NombreÉléments
    variables = [*vars_données, *vars_entête]


class UtilisationTerritoire(Fichier):
    nom = 'ls_regions.cal'
    division = DivisionUtilTerr
    sauter_ligne = True
