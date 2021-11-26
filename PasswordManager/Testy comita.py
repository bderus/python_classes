import os
dupa = 1
plik = open('password', 'w')
userName = input("Please insert your Username: ")
plik.write("Please insert your Username: " "|" + userName)

password = input("Please insert your Password: ")
plik.write("Please insert your Password: " "|" + password)

def add():


    # implement a method which gets two inputs from user: Username and Password,
    # and then saves it in file named passwords.txt
    # the data should be saved in new line, separated by pipe sign, like: <name>|<pass>
    # the method should create the file if it doesn't exist
    # the method doesn't return anything
    pass