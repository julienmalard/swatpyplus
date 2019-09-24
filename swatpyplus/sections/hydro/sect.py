from swatpyplus.sect import Section
from .comp import Composantes
from .compte_obj import CompteObjet
from .hydrologie import Hydrologie
from .topographie import Topographie
from .champs import Champs


class Hydro(Section):
    fichiers = [Hydrologie, Topographie, Champs, CompteObjet, Composantes]
