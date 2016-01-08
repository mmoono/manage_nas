__author__ = 'dio'
#!/usr/bin/env python
import telnetlib
import time
import socket

HOST = "192.168.0.106"
username = "root"
password = "dupa123"


def test_telnet_status():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, 23))
        print("Telnet is up and running!")
        return True
    except socket.error as e:
        print('Telnet is down. Error message: %s' % e)
        return False
    s.close()


def shutdown_nas():
    tn = telnetlib.Telnet(HOST)
    tn.read_until("moono-nas login:")
    tn.write(username + "\n")
    tn.read_until("Password:")
    tn.write(password + "\n")
    tn.read_until("~ # ")
    tn.write("poweroff\n")
    tn.read_until("~ # ")
    tn.close()


def main():
    if test_telnet_status() is True:
        shutdown_nas()
    else:
        print('There is no need to shutdown NAS! Exiting...')
        exit(0)
    for retry in range(0, 61, 1):
        if retry == 60:
            print("There were some problems with shutting down NAS in 300 seconds!")
            exit(255)
        if test_telnet_status() is True:
            time.sleep(5)
        else:
            print('NAS was shutdown properly. Exiting')
            break
main()
