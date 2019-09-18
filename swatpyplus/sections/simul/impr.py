from swatpyplus.fichier import Fichier
from swatpyplus.variables import VarEntier, VarOuiNon, VarTexte


class AnnéesExclues(VarEntier):
    nom = 'Années exclues impression'
    cod = 'NYSKIP'


class JourInitial(VarEntier):
    nom = 'Jour initial impression'
    cod = 'DAY_START'


class AnnéeInitiale(VarEntier):
    nom = 'Année initiale impression'
    cod = 'YEAR_START'


class JourFinal(VarEntier):
    nom = 'Jour final impression'
    cod = 'DAY_END'


class AnnéeFinale(VarEntier):
    nom = 'Année finale impression'
    cod = 'YEAR_END'


class Interval(VarEntier):
    nom = 'Intervale impression'
    cod = 'INTERVAL'


class AnnéesMoyenne(VarEntier):
    nom = 'Années impression moyenne annuelle'
    cod = 'AA_NUMINT'


class VSV(VarOuiNon):
    nom = 'Impression format vsv (.csv)'
    cod = 'CSV'


class BD(VarOuiNon):
    nom = 'Impression format base de données'
    cod = 'BD'


class FDC(VarOuiNon):
    nom = 'Impression format de données commun (cdf)'
    cod = 'CDF'


class Sol(VarOuiNon):
    nom = 'Impression résultats sol'
    cod = 'SOIL'


class Gestion(VarOuiNon):
    nom = 'Impression résultats gestion'
    cod = 'MGT'


class ConexHydro(VarOuiNon):
    nom = 'Impression connectivité hydrographe'
    cod = 'HDYCON'


class CourbeDébit(VarOuiNon):
    nom = 'Impression courbe de débit'
    cod = 'FDC'


class Objets(VarTexte):
    nom = 'Objet à imprimer'
    cod = 'OBJECTS'


class Quotidienne(VarOuiNon):
    nom = 'Impression quotidienne'
    cod = 'DAILY'


class Mensuelle(VarOuiNon):
    nom = 'Impression mensuelle'
    cod = 'MONTHLY'


class Annuelle(VarOuiNon):
    nom = 'Impression annuelle'
    cod = 'YEARLY'


class MoyenneAnnuelle(VarOuiNon):
    nom = 'Impression moyennes annuelles'
    cod = 'AVANN'


vars_ = [
    AnnéesExclues, JourInitial, AnnéeInitiale, JourFinal, AnnéeFinale, Interval, AnnéesMoyenne, VSV, BD, FDC, Sol,
    Gestion, ConexHydro, CourbeDébit, Objets, Quotidienne, Mensuelle, Annuelle, MoyenneAnnuelle
]


class Imprimer(Fichier):
    nom = 'print.prt'
    variables = vars_
