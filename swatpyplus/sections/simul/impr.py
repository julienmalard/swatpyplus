from swatpyplus.div import Division
from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarOuiNon, VarTexte


class AnnéesExclues(VarEntier):
    nom = 'Années exclues impression'
    code = 'NYSKIP'


class JourInitial(VarEntier):
    nom = 'Jour initial impression'
    code = 'DAY_START'


class AnnéeInitiale(VarEntier):
    nom = 'Année initiale impression'
    code = 'YRC_START'


class JourFinal(VarEntier):
    nom = 'Jour final impression'
    code = 'DAY_END'


class AnnéeFinale(VarEntier):
    nom = 'Année finale impression'
    code = 'YRC_END'


class Interval(VarEntier):
    nom = 'Intervale impression'
    code = 'INTERVAL'


class AnnéesMoyenne(VarEntier):
    nom = 'Années impression moyenne annuelle'
    code = 'AA_NUMINT'


class VSV(VarOuiNon):
    nom = 'Impression format vsv (.csv)'
    code = 'CSV'


class BD(VarOuiNon):
    nom = 'Impression format base de données'
    code = 'DB'


class FDC(VarOuiNon):
    nom = 'Impression format de données commun (cdf)'
    code = 'NETCDF'


class Sol(VarOuiNon):
    nom = 'Impression résultats sol'
    code = 'SOIL'


class Gestion(VarOuiNon):
    nom = 'Impression résultats gestion'
    code = 'MGT'


class ConexHydro(VarOuiNon):
    nom = 'Impression connectivité hydrographe'
    code = 'HYDCON'


class CourbeDébit(VarOuiNon):
    nom = 'Impression courbe de débit'
    code = 'FDC'


class Objets(VarTexte):
    nom = 'Objet à imprimer'
    code = 'OBJECTS'


class Quotidienne(VarOuiNon):
    nom = 'Impression quotidienne'
    code = 'DAILY'


class Mensuelle(VarOuiNon):
    nom = 'Impression mensuelle'
    code = 'MONTHLY'


class Annuelle(VarOuiNon):
    nom = 'Impression annuelle'
    code = 'YEARLY'


class MoyenneAnnuelle(VarOuiNon):
    nom = 'Impression moyennes annuelles'
    code = 'AVANN'


class T(VarOuiNon):
    nom = 'Va donc savoir...'
    code = 'T'


vars_ = [
    AnnéesExclues, JourInitial, AnnéeInitiale, JourFinal, AnnéeFinale, Interval, AnnéesMoyenne, VSV, BD, FDC, Sol,
    Gestion, ConexHydro, CourbeDébit, Objets, Quotidienne, Mensuelle, Annuelle, MoyenneAnnuelle, T
]


class DivisionImprimer(Division):
    variables = vars_


class Imprimer(Fichier):
    nom = 'print.prt'
    division = DivisionImprimer
