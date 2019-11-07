from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel, VarEntier


class Nom(VarTexte):
    nom = "Nom de la voie d'eau gazonnée"
    code = 'NAME'


class IndicateurGazonnée(VarEntier):
    nom = "Indicateur de voie d'eau gazonnée (1= actif, 0= inactif"
    code = 'FLAG'


class ManningGazonnée(VarRéel):
    nom = "Constante de Manning pour les voies d'eau gazonnées"
    code = 'MANN'


class CoeffTransport(VarRéel):
    nom = "Coefficient de transport des sédiments défini par l'utilisateur"
    code = 'SED_CO'


class ProfondGazonnée(VarRéel):
    nom = "Profondeur de la voie d'eau gazonnée"
    code = 'DP'
    unité = 'm'


class LargeurGazonnée(VarRéel):
    nom = "Largeur de la voie d'eau gazonnée"
    code = 'WD'
    unité = 'mm/day'


class LongueurGazonnée(VarRéel):
    nom = "Longueur de la voie d'eau gazonnée"
    code = 'LEN'
    unité = 'km'


class PenteGazonnée(VarRéel):
    nom = "Pente de la voie d'eau gazonnée"
    code = 'SLP'
    unité = 'm/m'


vars_ = [Nom, IndicateurGazonnée, ManningGazonnée, CoeffTransport, ProfondGazonnée, LargeurGazonnée, LongueurGazonnée,
         PenteGazonnée]


class DivisionVoieGazonnée(Division):
    variables = vars_


class VoieGazonnée(Fichier):
    nom = 'grassedww.str'
    division = DivisionVoieGazonnée
