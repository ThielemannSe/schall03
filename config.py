# config.py
# 
# In dieser Datei werden die Konfigurationen der einzelnen Schienenfahrzeuge gespeichert.
# Im ersten Schritt passiert das lediglich fuer den ICE 3 Vollzug


ZUEGE = {
    'ICE3_VOLLZUG' : {
        'bezeichnung':      'ICE 3 - Vollzug',
        'fz-kategorie':     ['HGV_TRIEBZUG_2N', ],
        'fz-kat-anz' :      [2, ],
        'v_fz':             300,
        },
}


# Allgemein
FREQUENZEN = [63, 125, 250, 500, 1000, 2000, 4000, 8000]

GESCHWINDIGKEITSFAKTOR = {
    1  : [ -5,  -5,  -5,   0,  10,  25,  25,  25],
    2  : [ -5,  -5,  -5,   0,  10,  25,  25,  25],
    3  : [ -5,  -5,  -5,   0,  10,  25,  25,  25],
    4  : [ -5,  -5,  -5,   0,  10,  25,  25,  25],
    5  : [ 50,  50,  50,  50,  50,  50,  50,  50],
    6  : [ 50,  50,  50,  50,  50,  50,  50,  50],
    7  : [ 50,  50,  50,  50,  50,  50,  50,  50],
    8  : [-10, -10, -10, -10, -10, -10, -10, -10],
    9  : [-10, -10, -10, -10, -10, -10, -10, -10],
    10 : [ 20,  20,  20,  20,  20,  20,  20,  20],
    11 : [ 20,  20,  20,  20,  20,  20,  20,  20]
}

PEGELKORREKTUREN = [1, 1, 1, 4, -1, -4, -4, 1]


# HGV Triebzug (Ein-, Zwei-, und Drei-System-Version)
FZ_KATEGORIEN = {

'HGV_TRIEBZUG_1N' : {
    'n0' : 32,
    'tabelle' : [
        # Rollgeraeusche
        [ 1, 'schienerauheit',      -50, -40, -24, -8, -3,  -6, -11, -30, 73],
        [ 2, 'radrauheit',          -50, -40, -25, -9, -4,  -4, -11, -23, 62],
        # Aerodynamische Geraeusche (..._ad)
        [ 5, 'quellhoehe5m_ad',     -30, -21, -13, -9, -6,  -4,  -9, -17, 41],
        [ 6, 'ein-system-v_ad',     -27, -21, -12, -8, -5,  -5, -11, -19, 44],
        [ 7, 'quellhoehe0m_ad',     -16,  -9,  -7, -7, -7,  -9, -12, -17, 45],
        # Aggregatgeraeusche (..._ag)
        [ 8, 'quellhoehe4m_ag',     -35, -24, -13, -4, -5,  -7, -14, -25, 56],
        [ 9, 'quellhoehe0m_ag',     -35, -24, -10, -5, -5,  -8, -15, -26, 62],
        # Antriebsgeraeusche (..._at)
        [11, 'quellhoehe0m_at',     -32, -24,  -5, -4, -8, -12, -18, -29, 53],
        ]
},

'HGV_TRIEBZUG_2N' : {
    'n0' : 32,
    'tabelle' : [
        # Rollgeraeusche
        [ 1, 'schienerauheit',      -50, -40, -24, -8, -3,  -6, -11, -30, 73],
        [ 2, 'radrauheit',          -50, -40, -25, -9, -4,  -4, -11, -23, 62],
        # Aerodynamische Geraeusche (..._ad)
        [ 5, 'quellhoehe5m_ad',     -30, -21, -13, -9, -6,  -4,  -9, -17, 41],
        [ 6, 'zwei-system-v_ad',    -27, -21, -12, -8, -5,  -5, -11, -19, 46],
        [ 7, 'quellhoehe0m_ad',     -16,  -9,  -7, -7, -7,  -9, -12, -17, 45],
        # Aggregatgeraeusche (..._ag)
        [ 8, 'quellhoehe4m_ag',     -35, -24, -13, -4, -5,  -7, -14, -25, 56],
        [ 9, 'quellhoehe0m_ag',     -35, -24, -10, -5, -5,  -8, -15, -26, 62],
        # Antriebsgeraeusche (..._at)
        [11, 'quellhoehe0m_at',     -32, -24,  -5, -4, -8, -12, -18, -29, 53],
        ]
},

'HGV_TRIEBZUG_3N' : {
    'n0' : 32,
    'tabelle' : [
        # Rollgeraeusche
        [ 1, 'schienerauheit',      -50, -40, -24, -8, -3,  -6, -11, -30, 73],
        [ 2, 'radrauheit',          -50, -40, -25, -9, -4,  -4, -11, -23, 62],
        # Aerodynamische Geraeusche (..._ad)
        [ 5, 'quellhoehe5m_ad',     -30, -21, -13, -9, -6,  -4,  -9, -17, 41],
        [ 6, 'drei-system-v_ad',    -27, -21, -12, -8, -5,  -5, -11, -19, 47],
        [ 7, 'quellhoehe0m_ad',     -16,  -9,  -7, -7, -7,  -9, -12, -17, 45],
        # Aggregatgeraeusche (..._ag)
        [ 8, 'quellhoehe4m_ag',     -35, -24, -13, -4, -5,  -7, -14, -25, 56],
        [ 9, 'quellhoehe0m_ag',     -35, -24, -10, -5, -5,  -8, -15, -26, 62],
        # Antriebsgeraeusche (..._at)
        [11, 'quellhoehe0m_at',     -32, -24,  -5, -4, -8, -12, -18, -29, 53],
        ]
},
}