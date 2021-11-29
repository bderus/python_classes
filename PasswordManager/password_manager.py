import os


def add():
    plik = open('password', 'w')
    userName = input("Please insert your Username: ")
    plik.write("Username: " + userName + "\n")

    password = input("Please insert your Password: ")
    plik.write("Password: " + password)



def view():
    # implement a method which reads the file passwords.txt,
    # and then shows all Usernames and Password that are stored in it
    # in a nice formatted way, like Username: <name> | Password: <password>
    # the method should first check if the file exists
    # the method doesn't return anything
    pass



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), type q to quit ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
