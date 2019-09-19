import os

from .sections import sections


class Modèle(object):
    sections = sections

    def __init__(soimême, fichier):
        if os.path.isdir(fichier):
            fichier = os.path.join(fichier, 'file.cio')
        soimême.fichier = fichier
        soimême._lire()

    def écrire(soimême, fichier=None, forcer=False):
        fichier = fichier or soimême.fichier
        if fichier.endswith('file.cio'):
            fichier = os.path.dirname(fichier)
        if not os.path.isdir(fichier):
            os.makedirs(fichier)

    def obtenir_valeur(soimême, variable):
        pass

    def assigner_valeur(soimême):
        pass

    def _lire(soimême):
        pass
