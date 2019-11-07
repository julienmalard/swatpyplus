from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    code = 'NAME'


class TypSystème(VarRéel):
    nom = "Type de système septique"
    code = "TYP"


class AnnéeSystème(VarRéel):
    nom = "Année où le système septique est devenue opérationnelle"
    code = "YR"


class IndicateurSys(VarRéel):
    nom = "Indicateur de fonctionnement du système septique"
    code = "OPERATION"


class NombreResidents(VarRéel):
    nom = "Nombre de résidents permanents dans la maison"
    code = "RESIDENTS"


class SurfaceMoyenne(VarRéel):
    nom = "Surface moyenne du champ de drainage de chaque système septique"
    code = "AREA"
    unité = 'm2'


class TempsCorrigés(VarRéel):
    nom = "Temps jusqu'à ce que les systèmes défaillants soient corrigés"
    code = "T_FAIL"
    unité = 'days'


class ProfondeurBio(VarRéel):
    nom = "Profondeur au sommet de la couche de la zone bio à partir de la surface du sol"
    code = "DP_BIOZ"
    unité = 'mm'


class ÉpaisseurBio(VarRéel):
    nom = "Épaisseur de bi-ozone"
    code = "THK_BIOZ"
    unité = 'mm'


class DisSepRuisseau(VarRéel):
    nom = "Distance du système septique au ruisseau"
    code = "CHA_DIST"
    unité = 'km'


class NombresSystèmes(VarRéel):
    nom = "Nombres des systèmes septiques par kilomètre carré"
    code = "SEP_DENS"


class DensitéBio(VarRéel):
    nom = "Densité de la biomasse"
    code = "BM_DENS"
    unité = 'kg/m3'


class CoeffDBO(VarRéel):
    nom = "Coefficient de taux de décomposition de la DBO"
    code = "BOD_DECAY"
    unité = 'm3/day'


class ConvCroissanceBact(VarRéel):
    nom = "Facteur de conversion représentant la proportion de croissance bactérienne en masse et de DBO en masse " \
          "dégradée dans le STE "
    code = "BOD_CONV"


class CoeffLinéaire(VarRéel):
    nom = "Coefficient linéaire pour le calcul de la capacité de champ dans la zone bio"
    code = "FC_LIN"


class CoeffCapBio(VarRéel):
    nom = "Coefficient exponentiel pour le calcul de la capacité de champ dans la zone bio"
    code = "FC_EXP"


class CoeffFec(VarRéel):
    nom = "Coefficient du taux de décomposition des bactéries coliformes fécales"
    code = "FECAL_DECAY"
    unité = 'm3/day'


class FacteurTDS(VarRéel):
    nom = "Facteur de conversion pour la plaque de TDS"
    code = "TDS_CONV"


class CoeffMortal(VarRéel):
    nom = "Coefficient de taux de mortalité"
    code = "MORT"


class CoeffResp(VarRéel):
    nom = "Coefficient de fréquence respiratoire"
    code = "RESP"


class ParamSlough1(VarRéel):
    nom = "Première Paramètre de calibration slough-off"
    code = "SLOUGH1"


class ParamSlough2(VarRéel):
    nom = "Deuxième Paramètre de calibration slough-off"
    code = "SLOUGH2"


class CoeffNitrif(VarRéel):
    nom = "Coefficient de taux de nitrification"
    code = "NIT"


class CoeffDénitrif(VarRéel):
    nom = "Coefficient de taux de dénitrification"
    code = "DENIT"


class CoeffSorpP(VarRéel):
    nom = "Coefficient de répartition linéaire de la sorption du phosphore"
    code = "P_SORP"
    unité = 'L/kg'


class CoeffMaxSorpP(VarRéel):
    nom = "Capacité maximale de sorption de phosphore"
    code = "P_SORP_MAX"
    unité = 'mg P/kg soil'


class PenteÈqP(VarRéel):
    nom = "Pente de l'équation du phosphore soluble dans l'effluent linéaire"
    code = "SOLP_SLP"


class InterÈqP(VarRéel):
    nom = "Interception de l'équation du phosphore soluble dans l'effluent linéaire"
    code = "SOLP_INT"


vars_ = [Nom, TypSystème, AnnéeSystème, IndicateurSys, NombreResidents, SurfaceMoyenne, TempsCorrigés, ProfondeurBio,
         ÉpaisseurBio, DisSepRuisseau, NombresSystèmes, DensitéBio, CoeffDBO, ConvCroissanceBact, CoeffLinéaire,
         CoeffCapBio, CoeffFec, FacteurTDS, CoeffMortal, CoeffResp, ParamSlough1, ParamSlough2, CoeffNitrif,
         CoeffDénitrif, CoeffSorpP, CoeffMaxSorpP, PenteÈqP, InterÈqP]


class DivisionSeptiques(Division):
    variables = vars_


class Septiques(Fichier):
    nom = 'tiledrain.str'
    division = DivisionSeptiques
