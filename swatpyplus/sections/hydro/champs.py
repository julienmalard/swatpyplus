from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom'
    cod = 'name'


class LongChamp(VarRéel):
    nom = 'longueur du champ'
    cod = 'LEN'
    unité = 'm'


class LargChamp(VarRéel):
    nom = 'largeur du champ'
    cod = 'WD'
    unité = 'm'


class AngChamp(VarRéel):
    nom = 'Angle du champ'
    cod = 'ANG'
    unité = 'deg'


vars_ = [
    Nom, LongChamp, LargChamp, AngChamp
]

class Champs(Fichier):
    nom = 'field.fld'
    variables = vars_

