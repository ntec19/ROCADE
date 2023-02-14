# ROCADE

_Réveil Orchestré et Configuration A Distance Des Equipements_

_v2023-02-12d_

----

## Présentation

Le projet consiste à fournir une solution en Python pour :

- réveiller, par WOL, des PC éteints, à partir d'une liste d'adresses MAC

- scanner le réseau pour vérifier que les hôtes sont bien démarrés

- lancer sur toutes ces machines une ou plusieurs mêmes commandes

----

## Structure du projet

- Le fichier `config.py` contient les constantes et; en particulier, la liste des adresses MAC à réveiller.

- Le fichier `wakeup.py` permet d'envoyer le `magic packet WOL` à toutes les adresses physiques concernées. La bibliothèque Python [`wakeonlan`](https://pypi.org/project/wakeonlan/) est nécessaire.

- Le fichier `scan.py` permet, s'il est appelé directement, de lister les PC allumés (nom, adresse MAC, adresse IP). Lorsqu'il est importé, il a pour objet de fournir le dictionnaire `dict_resultat` au script appelant. La bibliothèque [`nmap`](https://pypi.org/project/python-nmap/) est nécessaire.

- Le fichier `remote.py` exécute à distance _(via ssh)_ une ou plusieurs mêmes commandes sur les PC concernés. La bibliothèque [`paramiko`](https://pypi.org/project/paramiko/) est nécessaire.

----

fin
