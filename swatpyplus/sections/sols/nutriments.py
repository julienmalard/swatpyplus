from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    code = 'NAME'


class CoeffProf(VarRéel):
    nom = 'Coefficient de profondeur pour ajuster la concentration pour le profondeur'
    code = 'DP_CO'


class AzoteTotale(VarRéel):
    nom = "Azote total à la surface du sol"
    code = 'TOT_N'
    unité = 'ppm'


class AzoteInorgan(VarRéel):
    nom = "Azote inorganique à la surface du sol"
    code = 'MIN_N'
    unité = 'ppm'


class AzoteOrgan(VarRéel):
    nom = "Azote Organique à la surface du sol"
    code = 'ORGN'
    unité = 'ppm'


class PhosTotal(VarRéel):
    nom = "Phosphore total à la surface du sol"
    code = 'TOT_P'
    unité = 'ppm'


class PhosInorgan(VarRéel):
    nom = "Phosphore inorganique à la surface du sol"
    code = 'MIN_P'
    unité = 'ppm'


class PhosOrgan(VarRéel):
    nom = "Phosphore organique à la surface du sol"
    code = 'ORG_P'
    unité = 'ppm'


class PhosEau(VarRéel):
    nom = "Phosphore solube dans l'eau à la surface du sol"
    code = "SOL_P"
    unité = 'ppm'


class PhosH3A(VarRéel):
    nom = "Phosphore H3A à la surface du sol"
    code = "H3A_P"
    unité = 'ppm'


class PhosMeh(VarRéel):
    nom = "Phosphore Mehlich à la surface du sol"
    code = "MEHL_P"
    unité = 'ppm'


class PhosBray(VarRéel):
    nom = "Phosphore Bray à la surface du sol"
    code = 'BRAY_P'
    unité = 'ppm'


vars_ = [Nom, CoeffProf, AzoteTotale, AzoteInorgan, AzoteOrgan, PhosTotal, PhosOrgan, PhosInorgan, PhosEau, PhosH3A,
         PhosMeh, PhosBray]


class DivisionNutriments(Division):
    variables = vars_


class NutriSol(Fichier):
    nom = 'nutrients.sol'
    division = DivisionNutriments
