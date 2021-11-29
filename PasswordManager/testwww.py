import os

try:
   check = open('password', 'r' )
except:
    print('Error plik nie istnieje ')


plik = open('password')

for linia in plik:
    print(linia)



"""
def view():
    # implement a method which reads the file passwords.txt,
    # and then shows all Usernames and Password that are stored in it
    # in a nice formatted way, like Username: <name> | Password: <password>
    # the method should first check if the file exists
    # the method doesn't return anything
    pass
"""