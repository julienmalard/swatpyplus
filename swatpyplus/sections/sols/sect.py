from swatpyplus.sect import Section
from .charac import CharacSols
from .nutriments import NutriSol
from .solslte import SolsLTE


class Sols(Section):
    nom = 'soils'
    fichiers = [CharacSols, NutriSol, SolsLTE]
