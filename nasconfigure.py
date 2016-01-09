#!/usr/bin/env python

import socket
import shelve
import naspass
from getpass import getpass

def is_valid_ipv4_address(address):
    '''
    Solution found at http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    :param address: string to be validated
    :return: True if string is IPv4 address, False if not
    '''
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True


def initialize_shelf():
    s = shelve.open("../config.dat")
    try:
        existing = s['mac']
        if existing and s['mac'] == None:
            raise ValueError('MAC address is empty')
    except:
        s['mac'] = None
    try:
        existing = s['broadcast']
        if existing and s['broadcast'] == None:
            raise ValueError('Broadcast address is empty')
    except:
        s['broadcast'] = None
    try:
        existing = s['user']
        if existing and s['user'] == None:
            raise ValueError('NAS username is empty')
    except:
        s['user'] = None
    s.close()


def print_current_setup():
    s = shelve.open('config.dat')
    print("NAS MAC: {0}\nNetwork broadcast: {1}\nNAS username: {2}\n".format(s['mac'], s['broadcast'], s['user']))
    s.close()



def change_mac():
    macaddress = raw_input("Enter new NAS MAC address: ")
    try:
        if len(macaddress) == 12:
            macaddress = macaddress.upper()
            pass
        elif len(macaddress) == 12 + 5:
            sep = macaddress[2]
            macaddress = macaddress.replace(sep, '').upper()
        else:
            raise ValueError('Incorrect MAC address format')
    except ValueError:
        return False
    return macaddress


def configure_mac():
    macaddress = False
    while not macaddress:
        macaddress = change_mac()
        if not macaddress:
            print("You have provided incorrect MAC address {}, please retry.".format(str(macaddress)))
    return macaddress


def configure_broadcast():
    address = raw_input("Enter new broadcast address: ")
    is_valid = is_valid_ipv4_address(address)
    while not is_valid:
        print("You have provided not valid IPv4 broadcast, please retry.")
        address = raw_input("Enter new broadcast address: ")
        is_valid = is_valid_ipv4_address(address)
    return address


def configure_username():
    username = raw_input("Provide NAS username (with rights to run \"poweroff\"")
    return username


def configure_password():
    secret = naspass.NasPass()
    paintextpass = getpass("Provide NAS password ")
    encPWD = secret.encryptPassword(paintextpass)
    file = open("../passwd.bin", "wb")
    file.write(encPWD)
    file.close
    print "Password file passwd.bin was created in parent directory."


def change_configuration(choice):
    s = shelve.open('config.dat')
    if int(choice) == 1:
        macaddress = configure_mac()
        s['mac'] = macaddress
    elif int(choice) == 2:
        address = configure_broadcast()
        s['broadcast'] = address
    elif int(choice) == 3:
        s['user'] = configure_username()
        configure_password()
    elif int(choice) == 4:
        macaddress = configure_mac()
        address = configure_broadcast()
        username = configure_username()
        configure_password()
        s['mac'] = macaddress
        s['broadcast'] = address
        s['user'] = username
    s.close()

if __name__ == '__main__':
    initialize_shelf()
    print_current_setup()
    change_configuration(4)
