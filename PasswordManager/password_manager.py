import os


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
