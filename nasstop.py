#!/usr/bin/env python
import telnetlib
import time
import socket


def test_telnet_status(host, timeout=5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, 23))
        print("Telnet is up and running!")
        return True
    except socket.error as e:
        print('Telnet did not respond in {} seconds. Error message: {}'.format(timeout, e))
        return False
    s.close()


def run_shutdown_nas(host, username, password):
    tn = telnetlib.Telnet(host)
    tn.read_until("login:")
    tn.write(username + "\n")
    tn.read_until("Password:")
    tn.write(password + "\n")
    tn.read_until("~ # ")
    tn.write("poweroff\n")
    tn.read_until("~ # ")
    tn.close()


def shutdown_nas(host, username, password):
    if test_telnet_status(host):
        run_shutdown_nas(host, username, password)
    else:
        print('There is no need to shutdown NAS! Exiting...')
        exit(0)
    for retry in range(0, 61, 1):
        if retry == 60:
            print("There were some problems with shutting down NAS in 300 seconds!")
            exit(255)
        if test_telnet_status(host):
            time.sleep(5)
        else:
            print('NAS was shutdown properly. Exiting')
            break
