from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du sol'
    code = 'TEXT'
    valeurs = ['sand', 'loamy_sand', 'sandy_loam', 'loam', 'silt_loam', 'silt', 'silty_clay', 'clay_loam',
               'sandy_clay_loam', 'sandy_clay', 'silty_clay', 'clay']


class CapacitéEau(VarRéel):
    nom = "Capacité en eau disponible pour le bassin versant LTE"
    code = "AWC"
    unité = 'mm/mm'


class PorositéSol(VarRéel):
    nom = "Porosité pour le sol LTE"
    code = "POR"
    unité = 'mm/mm'


class ConductivitéSol(VarRéel):
    nom = "Conductivité saturée pour le sol LTE"
    code = "SCON"
    unité = 'mm/hr'


vars_ = [Nom, CapacitéEau, PorositéSol, ConductivitéSol]


class DivisionSolsLTE(Division):
    variables = vars_


class SolsLTE(Fichier):
    nom = 'soils-lte.sol'
    division = DivisionSolsLTE
