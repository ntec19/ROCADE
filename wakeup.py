#!/usr/bin/env python3


from time import sleep as pause
try:
    # import du module wakeonlan
    # ajouté par pip (et non par apt install python3-xxx)
    # https://pypi.org/project/wakeonlan/
    # import wakeonlan
    from wakeonlan import send_magic_packet as wol
except:
    print("module 'wakeonlan' non importé -> exit")
    exit
from config import *


################################################################
# envoi N fois du 'magic packet'
N = 3
for i in range(N):
    print(f"Envoi du 'magic packet WOL' à toutes les valeurs dans 'DICT_MAC', passage {i+1} sur {N}...")
    for nom, mac in DICT_MAC.items():
        print("\t", nom, "->>", mac)
        wol(mac)
        pause(TEMPO_COURT)
    pause(TEMPO_LONG)
