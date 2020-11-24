# emission.py
# 
# Dieses Skript dient zur Berechnung der durch ein bestimmtes Schienenfahrzeug 
# erzeugten Schallleistung nach der gestzlichen Vorgabe "Schall03".

from math import log10
import numpy as np
from config import *



def anzAchsen(bez):
    pass

def ausgangsleistung(bez):
    fz = ZUEGE[bez] 
    vfz = fz['v_fz']
    for i, bez in enumerate(fz['fz-kategorie']):
        n0 = FZ_KATEGORIEN[bez]['n0']
        n = fz['fz-kat-anz'][i]
        quellen = FZ_KATEGORIEN[bez]['tabelle']
        fz_arr = []
        for q in quellen:
            q_arr = []
            m = q[0]
            a = q[-1]
            for j in range(0, 8):
                res = round(q[j+2] + a + 10 * log10(n0*n/n0) + PEGELKORREKTUREN[j] + log10(vfz/100), 5)
                q_arr.append(res)

            fz_arr.append(q_arr)
    return fz_arr


res = ausgangsleistung('ICE3_VOLLZUG')

for r in res:
    print(r)