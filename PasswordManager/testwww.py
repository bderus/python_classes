import sys


#def view():
    # implement a method which reads the file passwords.txt,
    # and then shows all Usernames and Password that are stored in it
    # in a nice formatted way, like Username: <name> | Password: <password>
    # the method should first check if the file exists
    # the method doesn't return anything
 #   pass



import os
def dupa():
    try:
        check = open('password','r')
    except OSError:
        print('Error plik nie istnieije ')
        sys.exit()

plik = open('password')
curses='red'
for linia in plik:
    print ( linia)

    pass
