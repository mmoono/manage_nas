#!/usr/bin/env python
import nasmenu
from start_with_wol import wake_on_lan
import shelve

if __name__ == '__main__':
    nasmenu.print_greetings()
    user_input = nasmenu.print_menu("Main menu", nasmenu.main_menu_options)
    print(user_input)
    while int(user_input) <> 0:
        if int(user_input) == 1:
            s = shelve.open('../config.dat')
            print("\nSending magic packet to MAC {}".format(s['mac']))
            wake_on_lan(s['mac'], s['broadcast'])
            s.close()
        elif int(user_input) == 2:
            print(" ")
            # TODO: stop nas
        elif int(user_input) == 3:
            execfile('nasconfigure.py')
       #elif int(user_input) == 0:
       #     print("Exiting.\nBye!")
       #     exit(0)
        user_input = nasmenu.print_menu("Main menu", nasmenu.main_menu_options)
    if int(user_input) == 0:
        print("Exiting.\nBye!")
        exit(0)