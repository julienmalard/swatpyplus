from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarTexte, VarRéel


class Nom(VarTexte):
    nom = 'Nom du nutriment'
    cod = 'NAME'


class TypSystème(VarRéel):
    nom = "Type de système septique"
    cod = "TYP"


class AnnéeSystème(VarRéel):
    nom = "Année où le système septique est devenue opérationnelle"
    cod = "YR"


class IndicateurSys(VarRéel):
    nom = "Indicateur de fonctionnement du système septique"
    cod = "OPERATION"


class NombreResidents(VarRéel):
    nom = "Nombre de résidents permanents dans la maison"
    cod = "RESIDENTS"


class SurfaceMoyenne(VarRéel):
    nom = "Surface moyenne du champ de drainage de chaque système septique"
    cod = "AREA"
    unité = 'm2'


class TempsCorrigés(VarRéel):
    nom = "Temps jusqu'à ce que les systèmes défaillants soient corrigés"
    cod = "T_FAIL"
    unité = 'days'


class ProfondeurBio(VarRéel):
    nom = "Profondeur au sommet de la couche de la zone bio à partir de la surface du sol"
    cod = "DP_BIOZ"
    unité = 'mm'


class ÉpaisseurBio(VarRéel):
    nom = "Épaisseur de bi-ozone"
    cod = "THK_BIOZ"
    unité = 'mm'


class DisSepRuisseau(VarRéel):
    nom = "Distance du système septique au ruisseau"
    cod = "CHA_DIST"
    unité = 'km'


class NombresSystèmes(VarRéel):
    nom = "Nombres des systèmes septiques par kilomètre carré"
    cod = "SEP_DENS"


class DensitéBio(VarRéel):
    nom = "Densité de la biomasse"
    cod = "BM_DENS"
    unité = 'kg/m3'


class CoeffDBO(VarRéel):
    nom = "Coefficient de taux de décomposition de la DBO"
    cod = "BOD_DECAY"
    unité = 'm3/day'


class ConvCroissanceBact(VarRéel):
    nom = "Facteur de conversion représentant la proportion de croissance bactérienne en masse et de DBO en masse " \
          "dégradée dans le STE "
    cod = "BOD_CONV"


class CoeffLinéaire(VarRéel):
    nom = "Coefficient linéaire pour le calcul de la capacité de champ dans la zone bio"
    cod = "FC_LIN"


class CoeffCapBio(VarRéel):
    nom = "Coefficient exponentiel pour le calcul de la capacité de champ dans la zone bio"
    cod = "FC_EXP"


class CoeffFec(VarRéel):
    nom = "Coefficient du taux de décomposition des bactéries coliformes fécales"
    cod = "FECAL_DECAY"
    unité = 'm3/day'


class FacteurTDS(VarRéel):
    nom = "Facteur de conversion pour la plaque de TDS"
    cod = "TDS_CONV"


class CoeffMortal(VarRéel):
    nom = "Coefficient de taux de mortalité"
    cod = "MORT"


class CoeffResp(VarRéel):
    nom = "Coefficient de fréquence respiratoire"
    cod = "RESP"


class ParamSlough1(VarRéel):
    nom = "Première Paramètre de calibration slough-off"
    cod = "SLOUGH1"


class ParamSlough2(VarRéel):
    nom = "Deuxième Paramètre de calibration slough-off"
    cod = "SLOUGH2"


class CoeffNitrif(VarRéel):
    nom = "Coefficient de taux de nitrification"
    cod = "NIT"


class CoeffDénitrif(VarRéel):
    nom = "Coefficient de taux de dénitrification"
    cod = "DENIT"


class CoeffSorpP(VarRéel):
    nom = "Coefficient de répartition linéaire de la sorption du phosphore"
    cod = "P_SORP"
    unité = 'L/kg'


class CoeffMaxSorpP(VarRéel):
    nom = "Capacité maximale de sorption de phosphore"
    cod = "P_SORP_MAX"
    unité = 'mg P/kg soil'


class PenteÈqP(VarRéel):
    nom = "Pente de l'équation du phosphore soluble dans l'effluent linéaire"
    cod = "SOLP_SLP"


class InterÈqP(VarRéel):
    nom = "Interception de l'équation du phosphore soluble dans l'effluent linéaire"
    cod = "SOLP_INT"


vars_ = [Nom, TypSystème, AnnéeSystème, IndicateurSys, NombreResidents, SurfaceMoyenne, TempsCorrigés, ProfondeurBio,
         ÉpaisseurBio, DisSepRuisseau, NombresSystèmes, DensitéBio, CoeffDBO, ConvCroissanceBact, CoeffLinéaire,
         CoeffCapBio, CoeffFec, FacteurTDS, CoeffMortal, CoeffResp, ParamSlough1, ParamSlough2, CoeffNitrif,
         CoeffDénitrif, CoeffSorpP, CoeffMaxSorpP, PenteÈqP, InterÈqP]


class Drainesdestuiles(Fichier):
    nom = 'tiledrain.str'
    variables = vars_
