from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom'
    code = 'NAME'


class TempNeige(VarRéel):
    nom = "Température de la neige"
    code = 'FALL_TMP'
    unité = 'deg C'


class TempBasNeige(VarRéel):
    nom = "Température de base de la fonte des neiges"
    code = 'MELT_TMP'
    unité = 'deg C'


class TauxFonteMax(VarRéel):
    nom = "Taux de fonte maximum de la neige au cours de l'année (21 juin)"
    code = 'MELT_MAX'
    unité = 'mm/deg C/day'


class TauxFonteMin(VarRéel):
    nom = "Taux de fonte minimum de la neige au cours de l'année (21 Décembre)"
    code = 'MELT_MIN'
    unité = 'mm/deg C/day'


class FacteurRetTemp(VarRéel):
    nom = "Facteur de retard de la température du manteau neigeux"
    code = 'TMP_LAG'


class TeneurEauMin(VarRéel):
    nom = "Teneur minimale en eau de la neige"
    code = 'SNOW_H2O'
    unité = 'mm'


class TeneurMinFraction(VarRéel):
    nom = "Fraction de la teneur minimale en eau de la neige"
    code = 'COV50'


class TeneurEauInitial(VarRéel):
    nom = "Teneur en eau initiale dans la neige au début de la simulation"
    code = 'SNOW_INIT'
    unité = 'mm'


vars_ = [Nom, TempNeige, TempBasNeige, TauxFonteMax, TauxFonteMin, FacteurRetTemp, TeneurEauMin, TeneurMinFraction,
         TeneurEauInitial]


class DivisionNeige(Division):
    variables = vars_


class Neige(Fichier):
    nom = 'snow.sno'
    division = DivisionNeige
