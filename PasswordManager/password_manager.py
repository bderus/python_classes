import os

import config
import app


def add():
    # implement a method which gets two inputs from user: Username and Password,
    # and then saves it in file named passwords.txt
    # the data should be saved in new line, separated by pipe sign, like: <name>|<pass>
    # the method should create the file if it doesn't exist
    # the method doesn't return anything
    pass


def view():
    # implement a method which reads the file passwords.txt,
    # and then shows all Usernames and Password that are stored in it
    # in a nice formatted way, like Username: <name> | Password: <password>
    # the method should first check if the file exists
    # the method doesn't return anything
    pass


def passwords_menu():
    mode = input(config.selected_language.get_passwords_menu_info())
    if mode == "q":
        app.main_menu()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print(config.selected_language.get_wrong_option_info())
        passwords_menu()
