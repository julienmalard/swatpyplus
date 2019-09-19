from swatpyplus.sect import Section
from .charac import CharacSols


class Sols(Section):
    nom = 'soils'
    fichiers = [CharacSols, ]
