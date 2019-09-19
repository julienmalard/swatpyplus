import os

from swatpyplus.div import DivisionPartition


class Fichier(object):
    nom = ''
    division = NotImplemented
    sauter_ligne = False

    def __init__(soimême, chemin):
        if not chemin.endswith(soimême.nom):
            soimême.chemin = os.path.join(chemin, soimême.nom)
        else:
            soimême.chemin = chemin
        soimême.titre = None
        soimême._structure = []
        soimême._lire()

    def modifié(soimême):
        return any(v.modifié for v in soimême._structure)

    def _lire(soimême):
        with open(soimême.chemin, mode='r', encoding='utf8') as d:
            l_0 = d.readline().split(':', maxsplit=1)
            if len(l_0) > 1:
                soimême.titre = l_0[1]

            if soimême.sauter_ligne:
                d.readline()

            lignes_div = []
            for l in d.readlines():
                if l:
                    lignes_div.append(l)
                else:
                    soimême._structure.append(soimême.division(lignes_div))
            if lignes_div:
                soimême._structure.append(soimême.division(lignes_div))
