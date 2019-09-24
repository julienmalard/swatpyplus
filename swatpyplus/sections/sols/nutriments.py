from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    cod = 'NAME'


class CoeffProf(VarRéel):
    nom = 'Coefficient de profondeur pour ajuster la concentration pour le profondeur'
    cod = 'DP_CO'


class AzoteTotale(VarRéel):
    nom = "Azote total à la surface du sol"
    cod = 'TOT_N'
    unité = 'ppm'


class AzoteInorgan(VarRéel):
    nom = "Azote inorganique à la surface du sol"
    cod = 'MIN_N'
    unité = 'ppm'


class AzoteOrgan(VarRéel):
    nom = "Azote Organique à la surface du sol"
    cod = 'ORGN'
    unité = 'ppm'


class PhosTotal(VarRéel):
    nom = "Phosphore total à la surface du sol"
    cod = 'TOT_P'
    unité = 'ppm'


class PhosInorgan(VarRéel):
    nom = "Phosphore inorganique à la surface du sol"
    cod = 'MIN_P'
    unité = 'ppm'


class PhosOrgan(VarRéel):
    nom = "Phosphore organique à la surface du sol"
    cod = 'ORG_P'
    unité = 'ppm'


class PhosEau(VarRéel):
    nom = "Phosphore solube dans l'eau à la surface du sol"
    cod = "SOL_P"
    unité = 'ppm'


class PhosH3A(VarRéel):
    nom = "Phosphore H3A à la surface du sol"
    cod = "H3A_P"
    unité = 'ppm'


class PhosMeh(VarRéel):
    nom = "Phosphore Mehlich à la surface du sol"
    cod = "MEHL_P"
    unité = 'ppm'


class PhosBray(VarRéel):
    nom = "Phosphore Bray à la surface du sol"
    cod = 'BRAY_P'
    unité = 'ppm'


vars_ = [Nom, CoeffProf, AzoteTotale, AzoteInorgan, AzoteOrgan, PhosTotal, PhosOrgan, PhosInorgan, PhosEau, PhosH3A,
         PhosMeh, PhosBray]


class NutriSol(Fichier):
    nom = 'nutrients.sol'
    variables = vars_

