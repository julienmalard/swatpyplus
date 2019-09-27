from swatpyplus.sect import Section
from .drainesdetuiles import Drainesdestuiles
from .filtrante import Filtrante
from .septiques import Septiques
from .utilisateurbmp import UtilisateurBMP
from .voiegazonnée import VoieGazonnée


class Struc(Section):
    fichiers = [Drainesdestuiles, Filtrante, Septiques, UtilisateurBMP, VoieGazonnée]
