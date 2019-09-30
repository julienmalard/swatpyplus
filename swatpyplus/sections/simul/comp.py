from swatpyplus.fichier import Fichier
from swatpyplus.div import Division
from swatpyplus.variables import VarEntier


class NombrePests(VarEntier):
    nom = "Nombre de pesticides simulés"
    code = 'NUM_PESTS'


vars_ = [NombrePests]


class DivisionComp(Division):
    variables = vars_


class Composantes(Fichier):
    nom = 'constituents.cs'
    division = DivisionComp
