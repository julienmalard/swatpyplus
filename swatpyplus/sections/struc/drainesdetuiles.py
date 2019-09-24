from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    cod = 'NAME'


class ProfondTube(VarRéel):
    nom = "Profondeur du tube de drainage à la surface du sol"
    cod = 'DP'
    unité = 'mm'


class TempDrainer(VarRéel):
    nom = "Temps nécessaire pour drainer le sol à la capacité du champ"
    cod = 'T_FC'
    unité = 'hrs'


class TempLatence(VarRéel):
    nom = "Temps de latence du drain"
    cod = 'LAG'
    unité = 'hrs'


class RayonDraines(VarRéel):
    nom = "Rayon effectif des drains"
    cod = 'RAD'
    unité = 'mm'


class DistanceTuiles(VarRéel):
    nom = "Distance entre deux tuyaux de drainage ou tuiles"
    cod = 'DIST'
    unité = 'mm'


class CoeffDrain(VarRéel):
    nom = "Coefficient de drainage"
    cod = 'DRAIN'
    unité = 'mm/day'


class CapPompe(VarRéel):
    nom = "Capacité de la pompe"
    cod = 'PUMP'
    unité = 'mm/hr'


class FacteurMulti(VarRéel):
    nom = "Facteur de multiplication pour déterminer la constante de saturation latérale à partir de la valeur " \
          "d'entrée de constante de saturation SWAT "
    cod = 'LAT_KSAT'


vars_ = [Nom, ProfondTube, TempDrainer, TempLatence, RayonDraines, DistanceTuiles, CoeffDrain, CapPompe, FacteurMulti]

class Drainesdestuiles(Fichier):
    nom = 'tiledrain.str'
    variables = vars_
