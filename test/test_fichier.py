import os
import unittest

from swatpyplus.sections import sections

_à_tester = [f for s in sections for f in s.fichiers]
_dossier = os.path.join(os.path.split(__file__)[0], 'rsrc')
_dossier_réf = os.path.join(_dossier, 'réf')


class TestFichier(unittest.TestCase):
    def test_lire(soimême):
        for f in _à_tester:
            for d in documents_compatibles(f.nom):
                with soimême.subTest(os.path.join(os.path.split(os.path.split(d)[0])[1], f.nom)):
                    o = f(d)
                    o


def documents_compatibles(nom):
    l_fichiers = []
    for racine, dirs, fichiers in os.walk(_dossier):
        for f in fichiers:
            if nom == os.path.split(f)[1]:
                l_fichiers.append(os.path.join(racine, f))

    return l_fichiers
