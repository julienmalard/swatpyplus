from swatpyplus.sect import Section
from .comp import Composantes
from .compte_obj import CompteObjet
from .charac import CharacSols
from .nutriments import NutriSol


class Sols(Section):
    nom = 'soils'
    fichiers = [CharacSols, NutriSol, CompteObjet, Composantes]
