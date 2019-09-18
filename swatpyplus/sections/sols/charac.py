from swatpyplus.div import DivisionPartitionAlignée
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte, VarCatégo, VarRéel


class Nom(VarTexte):
    nom = 'Nom du sol'
    cod = 'SNAM'


class NombreCouches(VarEntier):
    nom = 'Nombre de couches du sol'
    cod = 'NLY'


class GroupeHydro(VarCatégo):
    nom = 'Groupe hydrologique'
    cod = 'HYD_GRP'
    valeurs = ['A', 'B', 'C', 'D']


class ProfondeurMaxRacines(VarRéel):
    nom = 'Profondeur maximale racines'
    cod = 'ZMX'


class ExclusionAnions(VarRéel):
    nom = 'Fraction exclusion anions'
    cod = 'ANION_EXCL'


class VolumeMaxFissures(VarRéel):
    nom = 'Volume maximal fissures'
    cod = 'CRK'


class Texture(VarTexte):
    nom = 'Texture du sol'
    cod = 'TEXTURE'


class Profondeur(VarRéel):
    nom = 'Profondeur couche'
    cod = 'DEPTH'


class DensitéApparente(VarRéel):
    nom = 'Densité apparente'
    cod = 'BD'


class CapacitéEauDisponible(VarRéel):
    nom = "Capacité de l'eau disponible"
    cod = 'AWC'


class ConductivitéHydraulique(VarRéel):
    nom = 'Conductivité hydraulique en milieu saturé'
    cod = 'K'


class CarboneOrganique(VarRéel):
    nom = 'Teneur en carbone organique'
    cod = 'CBN'


class Argile(VarRéel):
    nom = 'Teneur en argile'
    cod = 'CLAY'


class Limon(VarRéel):
    nom = 'Teneur en limon'
    cod = 'SILT'


class Sable(VarRéel):
    nom = 'Teneur en sable'
    cod = 'SAND'


class Roches(VarRéel):
    nom = 'Pourcentage de roches'
    cod = 'ROCK'


class Albédo(VarRéel):
    nom = 'Albédo'
    cod = 'ALB'


class Érodabilité(VarRéel):
    nom = 'Érodabilité USLE'
    cod = 'USLE_K'


class ConductivitéÉlectrique(VarRéel):
    nom = 'Conductivité électrique'
    cod = 'EC'


class Calcium(VarRéel):
    nom = 'Calcium'
    cod = 'CAL'


class pH(VarRéel):
    nom = 'pH'
    cod = 'PH'


vars_entête = [
    Nom, NombreCouches, GroupeHydro, ProfondeurMaxRacines, ExclusionAnions, VolumeMaxFissures, Texture
]
vars_secondaires = [
    Profondeur, DensitéApparente, CapacitéEauDisponible, ConductivitéHydraulique, CarboneOrganique, Argile, Limon,
    Sable, Roches, Albédo, Érodabilité, ConductivitéÉlectrique, Calcium, pH
]


class DivisionCharacSols(DivisionPartitionAlignée):
    vars_entête = vars_entête
    vars_secondaires = vars_secondaires
    var_n_lignes = NombreCouches


class CharacSols(Fichier):
    nom = 'soils.sol'
    variables = [*vars_secondaires, *vars_entête]
    division = DivisionCharacSols
