from swatpyplus.sect import Section
from .hydrologie import Hydrologie
from .topographie import Topographie
from .champs import Champs


class Hydro(Section):
    fichiers = [Hydrologie, Topographie, Champs]
