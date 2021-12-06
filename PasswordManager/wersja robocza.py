"""import app

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

def gameBoard(player, row, column):
    for count, row in enumerate(board):
        print(numeracjaPionowa, row)

if playerChoice == "1":
    print("Rozpoczyna gracz pierwszy ")
    print("   a  b  c")
    gameBoard()


else:
    app.main_menu()
"""
board = [["*","*","*"],
         ["*","*","*"],
         ["*","*","*"]]
print("    0    1    2")

for count, row in enumerate(board):
    print(count, row)

def gameBoard(player=0, row=0, column=0):
    print("    0    1    2")

    board[row][column] = player
    for count, row in enumerate(board):
        print(count, row)
def gameScheme():

    while True:
        if winCheck() != True:

            playerChoice = input("Wybierz X lub O: ")
            if playerChoice == "X" or playerChoice == "0":

                while True:
                    playerChoicerow = input("Wybierz wiersz: ")
                    if playerChoicerow == "0" or playerChoicerow == "1" or playerChoicerow == "2":

                        while True:
                            playerChoicecolumn = input("Wybierz kolumnę: ")
                            if playerChoicecolumn == "0" or "1" or "2":
                                gameBoard(str(playerChoice), int(playerChoicerow), int(playerChoicecolumn))
                            break
                    break


def winCheck():
        if board[0][0] == board[1][1] == board[2][2] == "X":
            print("WIN")
        elif board[2][0] == board[1][1] == board[0][2] == "X":
            print("WIN")
        elif board[0][0] == board[0][1] == board[0][2] == "X":
            print("WIN")
        elif board[1][0] == board[1][1] == board[1][2] == "X":
            print("WIN")
        elif board[2][0] == board[2][1] == board[2][2] == "X":
            print("WIN")
        elif board[0][0] == board[1][0] == board[2][0] == "X":
            print("WIN")
        elif board[0][1] == board[1][1] == board[2][1] == "X":
            print("WIN")
        elif board[0][2] == board[1][2] == board[2][2] == "X":
            print("WIN")
        elif board[0][0] == board[1][1] == board[2][2] == "0":
            print("WIN")
        elif board[2][0] == board[1][1] == board[0][2] == "0":
            print("WIN")
        elif board[0][0] == board[0][1] == board[0][2] == "0":
            print("WIN")
        elif board[1][0] == board[1][1] == board[1][2] == "0":
            print("WIN")
        elif board[2][0] == board[2][1] == board[2][2] == "0":
            print("WIN")
        elif board[0][0] == board[1][0] == board[2][0] == "0":
            print("WIN")
        elif board[0][1] == board[1][1] == board[2][1] == "0":
            print("WIN")
        elif board[0][2] == board[1][2] == board[2][2] == "0":
            print("WIN")

gameScheme()





    






