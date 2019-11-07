from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom'
    code = 'NAME'


class EffMélange(VarRéel):
    nom = "Efficacité de mélange de l'opération de labourage"
    code = 'MIX_EFF'


class ProfMélange(VarRéel):
    nom = "Profondeur de mélange causée par le labourage"
    code = 'MIN_N'
    unité = 'MIX_DP'


class Rugosité(VarRéel):
    nom = "Rugosité aléatoire"
    code = 'ROUGH'
    unité = 'mm'


class RugositéCrête(VarRéel):
    nom = "Rugosité de la crête"
    code = 'RIDGE_HT'
    unité = 'mm'


class IntevalleCrête(VarRéel):
    nom = "Intervalle de crête (ou espacement des lignes)"
    code = 'RIDGE_SP'
    unité = 'mm'


vars_ = [Nom, EffMélange, ProfMélange, Rugosité, RugositéCrête, IntevalleCrête]


class DivisionLabourage(Division):
    variables = vars_


class Labourage(Fichier):
    nom = 'tillage.til'
    division = DivisionLabourage
