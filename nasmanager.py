#!/usr/bin/env python
import nasmenu

if __name__ == '__main__':
    nasmenu.print_greetings()
    user_input = nasmenu.print_menu("Main menu", nasmenu.main_menu_options)
    print(user_input)
    if int(user_input) == 1:
        print(" ")
        #TODO: start nas
    elif int(user_input) == 2:
        print(" ")
        # TODO: stop nas
    elif int(user_input) == 3:
        print("Starting file nasconfigure.py")
        execfile('nasconfigure.py')
    elif int(user_input) == 0:
        print("Exiting.\nBye!")
        exit(0)
