import os


class Simul(object):
    def __init__(soimême, fichier):
        if os.path.isdir(fichier):
            fichier = os.path.join(fichier, 'file.cio')
        soimême.fichier = fichier
