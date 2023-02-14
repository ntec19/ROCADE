#!/usr/bin/env python3


from scan import *

import paramiko
import threading
hotes = dict_resultat
#print(hotes)


def remotecmd(pc, host, port, user, pwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout = stdout.read().decode("utf-8")
    stderr = stderr.read().decode("utf-8")
    ssh.close()
    print(f"--------\n{pc} :\nSTDOUT: {stdout}\nSTDERR: {stderr}\n\n")
    return (stdout, stderr)


for k, v in dict_resultat.items():
    pc = k
    ip = v[1]
    if ip != 'off':
        t = threading.Thread(target=remotecmd, args=(pc, ip, PORT, USER, PASS, COMMANDE))
        t.start()
