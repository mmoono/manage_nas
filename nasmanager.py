#!/usr/bin/env python
import nasmenu
from start_with_wol import wake_on_lan
from nasstop import shutdown_nas
from naspass import NasPass
import shelve

if __name__ == '__main__':
    nasmenu.print_greetings()
    user_input = nasmenu.print_menu("Main menu", nasmenu.main_menu_options)
    print(user_input)
    while int(user_input) <> 0:
        if int(user_input) == 1:
            s = shelve.open('config.dat')
            print("\nSending magic packet to MAC {}".format(s['mac']))
            wake_on_lan(s['mac'], s['broadcast'])
            s.close()
        elif int(user_input) == 2:
            print("Shutting down NAS!\n")
            s = shelve.open('config.dat')
            secret = NasPass()
            file = open("passwd.bin", "r")
            encrypted_pass = file.read()
            decrypted_pass = secret.decryptPassword(encrypted_pass)
            file.close()
            shutdown_nas(s['ip'], s['user'], decrypted_pass)
            s.close()
        elif int(user_input) == 3:
            execfile('nasconfigure.py')
        user_input = nasmenu.print_menu("Main menu", nasmenu.main_menu_options)
    if int(user_input) == 0:
        print("Exiting.\nBye!")
        exit(0)