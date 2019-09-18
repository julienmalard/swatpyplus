from swatpyplus.sect import Section
from .comp import Composantes
from .compte_obj import CompteObjet
from .impr import Imprimer
from .impr_obj import ImprimerObjet
from .temps import Temps


class Simul(Section):
    fichiers = [Temps, Imprimer, ImprimerObjet, CompteObjet, Composantes]
