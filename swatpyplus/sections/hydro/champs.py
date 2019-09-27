from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom'
    code = 'NAME'


class LongChamp(VarRéel):
    nom = 'longueur du champ'
    code = 'LEN'
    unité = 'm'


class LargChamp(VarRéel):
    nom = 'largeur du champ'
    code = 'WD'
    unité = 'm'


class AngChamp(VarRéel):
    nom = 'Angle du champ'
    code = 'ANG'
    unité = 'deg'


vars_ = [
    Nom, LongChamp, LargChamp, AngChamp
]


class DivisionChamps(Division):
    variables = vars_


class Champs(Fichier):
    nom = 'field.fld'
    division = DivisionChamps
