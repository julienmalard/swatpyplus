from swatpyplus.div import DivisionPartitionAlignée
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarTexte, VarCatégo, VarRéel


class Nom(VarTexte):
    nom = 'Nom du sol'
    code = 'SNAM'


class NombreCouches(VarEntier):
    nom = 'Nombre de couches du sol'
    code = 'NLY'


class GroupeHydro(VarCatégo):
    nom = 'Groupe hydrologique'
    code = 'HYD_GRP'
    valeurs = ['A', 'B', 'C', 'D']


class ProfondeurMaxRacines(VarRéel):
    nom = 'Profondeur maximale racines'
    code = 'ZMX'


class ExclusionAnions(VarRéel):
    nom = 'Fraction exclusion anions'
    code = 'ANION_EXCL'


class VolumeMaxFissures(VarRéel):
    nom = 'Volume maximal fissures'
    code = 'CRK'


class Texture(VarTexte):
    nom = 'Texture du sol'
    code = 'TEXTURE'


class Profondeur(VarRéel):
    nom = 'Profondeur couche'
    code = 'DEPTH'


class DensitéApparente(VarRéel):
    nom = 'Densité apparente'
    code = 'BD'


class CapacitéEauDisponible(VarRéel):
    nom = "Capacité de l'eau disponible"
    code = 'AWC'


class ConductivitéHydraulique(VarRéel):
    nom = 'Conductivité hydraulique en milieu saturé'
    code = 'K'


class CarboneOrganique(VarRéel):
    nom = 'Teneur en carbone organique'
    code = 'CBN'


class Argile(VarRéel):
    nom = 'Teneur en argile'
    code = 'CLAY'


class Limon(VarRéel):
    nom = 'Teneur en limon'
    code = 'SILT'


class Sable(VarRéel):
    nom = 'Teneur en sable'
    code = 'SAND'


class Roches(VarRéel):
    nom = 'Pourcentage de roches'
    code = 'ROCK'


class Albédo(VarRéel):
    nom = 'Albédo'
    code = 'ALB'


class Érodabilité(VarRéel):
    nom = 'Érodabilité USLE'
    code = 'USLE_K'


class ConductivitéÉlectrique(VarRéel):
    nom = 'Conductivité électrique'
    code = 'EC'


class Calcium(VarRéel):
    nom = 'Calcium'
    code = 'CAL'


class pH(VarRéel):
    nom = 'pH'
    code = 'PH'


vars_entête = [
    Nom, NombreCouches, GroupeHydro, ProfondeurMaxRacines, ExclusionAnions, VolumeMaxFissures, Texture
]
vars_données = [
    Profondeur, DensitéApparente, CapacitéEauDisponible, ConductivitéHydraulique, CarboneOrganique, Argile, Limon,
    Sable, Roches, Albédo, Érodabilité, ConductivitéÉlectrique, Calcium, pH
]


class DivisionCharacSols(DivisionPartitionAlignée):
    vars_entête = vars_entête
    vars_données = vars_données
    var_n_lignes = NombreCouches


class CharacSols(Fichier):
    nom = 'soils.sol'
    variables = [*vars_données, *vars_entête]
    division = DivisionCharacSols
