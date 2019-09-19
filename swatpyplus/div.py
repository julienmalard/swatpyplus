import numpy as np
import pandas as pd


class Division(object):
    variables = []

    def __init__(soimême, d):
        soimême.données = None

        soimême._structure = soimême._lire(d)

    def _lire(soimême, d):
        struct = []
        codes = [v.code for v in soimême.variables]

        lignes = [d[0]]
        for l in d[1:]:
            itèmes = l.split()
            if all(i in codes for i in itèmes) or not l:
                struct.append(soimême._former_données(lignes, soimême.variables))
                lignes = [l]
            else:
                lignes.append(l)

        return struct

    @staticmethod
    def _former_données(d, variables, entête=None):
        cds = entête if entête else d[0].split()
        cds = [c for c in cds if c in [vr.code for vr in variables]]
        vars_ = [next(vr for vr in variables if vr.code == c) for c in cds]
        données = {vr.code: np.array(
            [l.split()[i] for l in d[0 if entête else 1:]],
            dtype=vr.dtype
        ) for i, vr in enumerate(vars_)}
        return pd.DataFrame(données)


class DivisionPartition(Division):
    vars_entête = []
    vars_données = []
    var_n_lignes = None

    def _lire(soimême, d):
        struct = {
            'entête': soimême._former_données(d[:2], soimême.vars_entête),
            'données': soimême._former_données(d[2:], soimême.vars_données)
        }

        return struct


class DivisionPartitionAlignée(DivisionPartition):
    def _lire(soimême, d):
        struct = []
        ligne_entête = d[0].split()
        i = 1
        while i < len(d):
            entête = soimême._former_données(d[i:i+1], soimême.vars_entête, entête=ligne_entête)
            n_lignes = entête[soimême.var_n_lignes.code][0]
            données = soimême._former_données(d[i+1:i+n_lignes+1], soimême.vars_données, entête=ligne_entête)
            i += n_lignes + 1
            struct.append({'entête': entête, 'données': données})
        return struct
