#!/usr/bin/env python3


COMMANDE    = 'sudo poweroff'
'''
sudo poweroff
sudo apt-get update && sudo apt-get -y upgrade
'''

RESEAU      = '192.168.0.0/24'
PORT        = 22
USER        = 'stage'
PASS        = '123'
TEMPO_COURT = 0.2
TEMPO_LONG  = 1

DICT_MAC = {
"DEB101" : "a0-8c-fd-e5-8f-07" ,
"DEB102" : "a0-8c-fd-d6-7f-01" ,
"DEB103" : "a0-8c-fd-e5-90-ae" ,
"DEB104" : "a0-8c-fd-d6-7f-c0" ,
"DEB105" : "a0-8c-fd-e7-05-25" ,
"DEB106" : "a0-8c-fd-e7-04-6f" ,
"DEB107" : "a0-8c-fd-e0-49-89" ,
"DEB108" : "a0-8c-fd-e7-04-bd" ,
"DEB109" : "a0-8c-fd-e0-4d-d2" ,
"DEB110" : "a0-8c-fd-e0-48-12" ,
"DEB111" : "a0-8c-fd-d6-7f-06" ,
"DEB112" : "a0-8c-fd-e7-05-70" ,
"DEB113" : "a0-8c-fd-e0-5d-23" ,
"DEB114" : "dc-4a-3e-4d-4e-dc" ,
"DEB115" : "dc-4a-3e-4d-49-62" ,
"BUREAU-LAN" : "dc-4a-3e-4d-41-4a" ,
"BUREAU-WLAN" : "00-22-2d-3c-d7-42"
}

