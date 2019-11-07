from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte


class Nom(VarTexte):
    nom = 'Nom'
    code = 'name'


vars_ = [Nom]


class DivisionCompteObj(Division):
    variables = vars_


class CompteObjet(Fichier):
    nom = 'object.cnt'
    division = DivisionCompteObj
