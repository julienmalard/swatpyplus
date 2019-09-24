from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte


class Numéro(VarEntier):
    nom = 'Numéro'
    cod = 'numb'


class TypeObjet(VarTexte):
    nom = "Type d'objet à imprimer"
    cod = 'obtyp'


class NumTypeObjet(VarEntier):
    nom = "Numéro de type d'objet"
    cod = 'obtypno'


class Hydrogramme(VarTexte):
    nom = "Type d'hydrogramme à imprimer"
    cod = 'hydtyp'


class NomFichier(VarTexte):
    nom = "Nom du fichier du sortie"
    cod = 'filename'


vars_ = [
    Numéro, TypeObjet, NumTypeObjet, Hydrogramme, NomFichier
]


class ImprimerObjet(Fichier):
    nom = 'object.prt'
    variables = vars_
