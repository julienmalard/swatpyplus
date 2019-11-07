from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom'
    code = 'name'


class ÉcouleLat(VarEntier):
    nom = "temps d'écoulement latéral"
    code = 'LAT_TTIME'
    unité = 'jour(s)'


class SédimentationLatérale(VarRéel):
    nom = "sédimentation latérale dans les écoulements latéraux et souterrains"
    code = 'LAT_SED'
    unité = "g/L"


class StokageMaximal(VarRéel):
    nom = 'stockage maximal de la canopée'
    code = 'CAN_MAX'
    unité = 'mm'


class CompensationÉvaporation(VarRéel):
    nom = "Facteur de compensation de l'évaporation du sol"
    code = 'ESCO'


class CompensationAdsorption(VarRéel):
    nom = "Facteur de compensation d'absorption par les plantes"
    code = 'EPCO'


class EnrichissementAzoteOrganique(VarRéel):
    nom = "Ratio d'enrichissement en azote organique pour le chargement avec des sédiments"
    code = 'ORGN_ENRICH'


class EnrichissementPhosphoreOrganique(VarRéel):
    nom = "Ratio d'enrichissement en azote organique pour le chargement avec des sédiments"
    code = 'ORGP_ENRICH'


class CoeffÉvaporationNidsPoule(VarRéel):
    nom = "Coefficient d'évaporation des nids de poule"
    code = "EVAP_POTHOLE"


class EficacitéBioMélange(VarRéel):
    nom = "Efficacité Biologique du Mélange"
    code = "BIO_MIX"


class CoeffPercolation(VarRéel):
    nom = "Coefficient de Percolation; ajuste l'humidité du sol pour que la percolation se produise"
    code = "PERCO"


class ConcAzoteLatéraux(VarRéel):
    nom = "Concentration d'azote organique dans les écoulements latéraux"
    code = "LAT_ORGN"
    unité = 'mg/L'


class CoeffPercolation(VarRéel):
    nom = "Concentration de phosphore organique dans les écoulements latéraux"
    code = "LAT_ORGP"
    unité = 'mg/L'


class CoeffHargreaves(VarRéel):
    nom = "Coefficient lié au rayonnement utilisé dans les équations de Hargreaves"
    code = "HARG_PET"


class NCEvapo(VarRéel):
    nom = "Numéro de courbe d'évapotranspiration des plantes"
    code = "CN_PLNTET"


vars_ = [
    Nom, ÉcouleLat, SédimentationLatérale, StokageMaximal, CompensationÉvaporation, CompensationAdsorption,
    EnrichissementAzoteOrganique, EnrichissementPhosphoreOrganique, CoeffÉvaporationNidsPoule, EficacitéBioMélange,
    CoeffPercolation, ConcAzoteLatéraux, CoeffPercolation, CoeffHargreaves, NCEvapo
]


class DivisionHydrologie(Division):
    variables = vars_


class Hydrologie(Fichier):
    nom = 'hydrology.hyd'
    division = DivisionHydrologie
