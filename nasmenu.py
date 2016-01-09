#!/usr/bin/env python


main_menu_options = ["Start NAS", "Shutdown NAS", "Configure NAS", "Exit\n"]
config_menu_options = ["Configure NAS MAC address", "Configure network broadcast", "Configure username and password",
                        "Run initial configuration", "Print current setup", "Exit to main menu\n"]


def print_greetings():
    greet_text = "Welcome to ZyXeL NSA310S management tool"
    print("#"*(len(greet_text)+4))
    print("# "+" "*len(greet_text)+" #")
    print("# "+greet_text.center(len(greet_text))+" #")
    print("# "+" "*len(greet_text)+" #")
    print("#"*(len(greet_text)+4))


def print_menu(menu_type, menu_options):
    index = 1
    print("\n{}:".format(menu_type))
    print("-"*(len(max(menu_options, key=len))+3))
    for option in menu_options:
        if option.startswith("Exit"):
            index = 0
        print("{}. {}".format(index, option))
        index += 1
    user_input = raw_input("Please select an operation: ")
    while not user_input.isalnum():
        user_input = raw_input("Wrong option, please retry: ")
    while int(user_input) > len(menu_options) - 1:
        user_input = raw_input("Wrong option, please retry: ")
        while not user_input.isalnum():
            user_input = raw_input("Wrong option, please retry: ")
    return user_input