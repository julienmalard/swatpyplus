class Division(object):
    variables = []

    def __init__(soimême, d):
        soimême.données = None

        soimême._lire(d)

    def _lire(soimême, d):
        pass


class DivisionPartition(Division):
    vars_entête = []
    vars_secondaires = []
    var_n_lignes = None


class DivisionPartitionAlignée(DivisionPartition):
    pass
