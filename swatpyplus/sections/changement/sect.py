from swatpyplus.sect import Section
from .régions_util import UtilisationTerritoire


class Changement(Section):
    nom = 'chg'
    fichiers = [UtilisationTerritoire, ]