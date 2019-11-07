from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte


class Numéro(VarEntier):
    nom = 'Numéro'
    code = 'numb'


class TypeObjet(VarTexte):
    nom = "Type d'objet à imprimer"
    code = 'obtyp'


class NumTypeObjet(VarEntier):
    nom = "Numéro de type d'objet"
    code = 'obtypno'


class Hydrogramme(VarTexte):
    nom = "Type d'hydrogramme à imprimer"
    code = 'hydtyp'


class NomFichier(VarTexte):
    nom = "Nom du fichier du sortie"
    code = 'filename'


vars_ = [
    Numéro, TypeObjet, NumTypeObjet, Hydrogramme, NomFichier
]


class DivisionImprimObj(Division):
    variables = vars_


class ImprimerObjet(Fichier):
    nom = 'object.prt'
    division = DivisionImprimObj
