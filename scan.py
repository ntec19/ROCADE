#!/usr/bin/env python3


import os
from config import *


# test si le contexte est 'root' (nécessaire pour le scan nmap)
if os.geteuid() != 0:
    exit("Ce script doit être exécuté avec les droits 'root'.")


try:
    import nmap
except:
    print("module 'nmap' non importé -> exit")
    exit


# Création d'un objet nmap.PortScanner
scanner = nmap.PortScanner()


# Scan du réseau
# DÉCOUVERTE DES HÔTES:
# -sP: Ping Scan - Ne fait que déterminer si les hôtes sont en ligne
# -n: Ne jamais résoudre les noms DNS
dict_scanner = scanner.scan(hosts=RESEAU, arguments='-sP -n')


# construire un dictionnaire {'ip': 'mac'}
# { 'a0-1b-29-7f-48-e5': '192.168.0.1', 'dc-4a-3e-4d-49-62': '192.168.0.113', etc. }
dict_IP_mac = {}
for v in dict_scanner['scan'].values():
    try:
        dict_IP_mac[v['addresses']['mac'].replace(':','-').lower()] =  v['addresses']['ipv4']
    except:
        pass


# filtrer le dictionnaire obtenu ci-dessus en ne conservant
# que les hôtes dont l'adresse MAC est dans la liste DICT_MAC
# { 'dc-4a-3e-4d-49-62': '192.168.0.113', etc. }
dict_IP_mac_liste = {}
for mac, ip in dict_IP_mac.items():
    if mac in DICT_MAC.values():
        dict_IP_mac_liste[mac] = ip


# construire un dictionnaire dict_resultat ainsi formé :
# { "DEB101" : ["a0-8c-fd-e5-8f-07" , "192.168.0.122"], etc.
dict_resultat = {}
for nom, mac in DICT_MAC.items():
    cle = nom
    if mac in dict_IP_mac_liste.keys():
        ip = dict_IP_mac_liste[mac]
    else:
        ip = 'off'
    dict_resultat[nom] = [ mac, ip ]


# si ce script est appelé directement (pas par 'import'), affichage :
if __name__ == "__main__":
    # affichage des PC allumés ET éteints
    print("\n-----------------------------------------------")
    print("    Bilan des ordinateurs allumés/éteints :    ")
    print("-----------------------------------------------")
    for k, v in dict_resultat.items():
        print(f"Ordinateur {k}\t: {v[0]}\t :  {v[1]}")
