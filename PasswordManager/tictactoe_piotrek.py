import app


def StartGame():
    print("Zaimplementuj mnie Piotrku!")
    TicTacToeMenu()


def TicTacToeMenu():
    user_option = input("Wybierz opcję - 1 by zacząć grę, 2 żeby wrócić:")
    if user_option == "2":
        app.main_menu()

    if user_option == "1":
        StartGame()


lista = [[0,0,0],[0,0,0],[0,0,0]]
    for i in lista
        print(lista)
