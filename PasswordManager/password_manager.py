import os

import config
import app


def add():
    with open('password.txt', 'a') as plik:
         userName = input("Please insert your Username: ")
         password = input("Please insert your Password: ")
         plik.write(userName + "|" + password + "\n")
    passwords_menu()


def view():
    x = os.path.exists("password.txt")
    if x == True:
        with open('password.txt', 'r') as file:
            for linia in file:
                print(linia)
    else:
        print("plik nie istnieje")


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
