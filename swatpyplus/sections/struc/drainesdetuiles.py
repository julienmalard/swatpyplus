from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    code = 'NAME'


class ProfondTube(VarRéel):
    nom = "Profondeur du tube de drainage à la surface du sol"
    code = 'DP'
    unité = 'mm'


class TempDrainer(VarRéel):
    nom = "Temps nécessaire pour drainer le sol à la capacité du champ"
    code = 'T_FC'
    unité = 'hrs'


class TempLatence(VarRéel):
    nom = "Temps de latence du drain"
    code = 'LAG'
    unité = 'hrs'


class RayonDraines(VarRéel):
    nom = "Rayon effectif des drains"
    code = 'RAD'
    unité = 'mm'


class DistanceTuiles(VarRéel):
    nom = "Distance entre deux tuyaux de drainage ou tuiles"
    code = 'DIST'
    unité = 'mm'


class CoeffDrain(VarRéel):
    nom = "Coefficient de drainage"
    code = 'DRAIN'
    unité = 'mm/day'


class CapPompe(VarRéel):
    nom = "Capacité de la pompe"
    code = 'PUMP'
    unité = 'mm/hr'


class FacteurMulti(VarRéel):
    nom = "Facteur de multiplication pour déterminer la constante de saturation latérale à partir de la valeur " \
          "d'entrée de constante de saturation SWAT "
    code = 'LAT_KSAT'


vars_ = [Nom, ProfondTube, TempDrainer, TempLatence, RayonDraines, DistanceTuiles, CoeffDrain, CapPompe, FacteurMulti]


class DivisionDrainesDeTuiles(Division):
    variables = vars_


class Drainesdestuiles(Fichier):
    nom = 'tiledrain.str'
    division = DivisionDrainesDeTuiles
