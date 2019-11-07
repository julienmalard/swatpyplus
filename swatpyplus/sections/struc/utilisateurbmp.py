from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel, VarEntier


class Nom(VarTexte):
    nom = "Nom du BMP de l'utilisateur (BMP: Meilleure pratique de gestion)"
    code = 'NAME'


class IndicateurBMP(VarEntier):
    nom = "Indicateur du BMP; 1=actif, 2=inactif"
    code = 'FLAG'


class SédimentBMP(VarRéel):
    nom = "Fraction de sédiment enlevé par BMP"
    code = 'SED_EFF'


class PhosPartBMP(VarRéel):
    nom = "Fraction de phosphore particulaire enlevée par le BMP"
    code = 'PTLP_EFF'


class PhosSolBMP(VarRéel):
    nom = "Fraction de phosphore soluble enlevée par BMPs"
    code = 'SOLP_EFF'


class AzoPartBMP(VarRéel):
    nom = "Fraction d'azote particulaire enlevée par BMPs"
    code = 'PTLN_EFF'


class AzoSolBMP(VarRéel):
    nom = "Fraction d'azote soluble enlevée par BMPs"
    code = 'SOLN_EFF'


class BactBMP(VarRéel):
    nom = "Fraction de bactéries enlevées par BMP"
    code = 'BACT_EFF'


vars_ = [Nom, IndicateurBMP, SédimentBMP, PhosPartBMP, PhosSolBMP, AzoPartBMP, AzoSolBMP, BactBMP]


class DivisionUtilisateurBMP(Division):
    variables = vars_


class UtilisateurBMP(Fichier):
    nom = 'bmpuser.str'
    division = DivisionUtilisateurBMP
