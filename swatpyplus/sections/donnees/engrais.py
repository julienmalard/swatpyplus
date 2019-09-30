from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom'
    code = 'NAME'


class EngrMinAzote(VarRéel):
    nom = "Fraction d'engrais constituée d'azote minéral (NO3+NH3)"
    code = 'MIN_N'


class EngrMinPhos(VarRéel):
    nom = "Fraction d'engrais constituée de phosphore minéral"
    code = 'MIN_P'


class EngrOrgAzote(VarRéel):
    nom = "Fraction d'engrais constituée d'azote organique"
    code = 'ORG_N'


class EngrOrgPhos(VarRéel):
    nom = "Fraction d'engrais constituée de phosphore organique"
    code = 'ORG_P'


class EngrNH3Azote(VarRéel):
    nom = "Fraction d'azote minéral de l'engrais qui est NH3"
    code = 'NH3_N'


class Pathogènes(VarTexte):
    nom = "Pathogènes"
    code = 'PATHOGENS'


vars_ = [Nom, EngrMinAzote, EngrMinPhos, EngrOrgAzote, EngrOrgPhos, EngrNH3Azote, Pathogènes]


class DivisionEngrais(Division):
    variables = vars_


class Engrais(Fichier):
    nom = 'fertilizer.frt'
    division = DivisionEngrais
