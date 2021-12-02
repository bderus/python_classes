import app

board = [[1,2,3],
         [1,2,3],
         [1,2,3]]
player = input("Wybierz X lub O: ")
if player == "X":
    print("Gracz pierwszy ma X, gracz drugi ma O ")
elif player == "O":
    print("Gracz pierwszy ma O, gracz drugi ma X ")
else:
    print("Nieprawidłowy wybór ")

playerChoice = input("Wybierz 1, aby rozpocząć grę, wybierz 2, aby wrócić do wyboru menu: ")

def gameBoard():
    for numeracjaPionowa, el in enumerate(board):
        print(numeracjaPionowa, el)

if playerChoice == "1":
    print("Rozpoczyna gracz pierwszy ")
    print("   a  b  c")
    gameBoard()


else:
    app.main_menu()









