import os


def add():
    with open('password.txt', 'a') as plik:
         userName = input("Please insert your Username: ")
         password = input("Please insert your Password: ")
         plik.write(userName + "|" + password + "\n")


def view():
    x = os.path.exists("password.txt")
    if x == True:
        with open('password.txt', 'r') as file:
            for linia in file:
                print(linia)
    else:
        print("plik nie istnieje")


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
