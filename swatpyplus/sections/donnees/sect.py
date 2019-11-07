from swatpyplus.sect import Section
from .engrais import Engrais
from .labourage import Labourage
from .neige import Neige


class Données(Section):
    fichiers = [Engrais, Labourage, Neige]
