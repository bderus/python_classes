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
        break

def winCheck():
        if board[0][0] == board[1][1] == board[2][2] == "X":
            return True
        elif board[2][0] == board[1][1] == board[0][2] == "X":
            return True
        elif board[0][0] == board[0][1] == board[0][2] == "X":
            return True
        elif board[1][0] == board[1][1] == board[1][2] == "X":
            return True
        elif board[2][0] == board[2][1] == board[2][2] == "X":
            return True
        elif board[0][0] == board[1][0] == board[2][0] == "X":
            return True
        elif board[0][1] == board[1][1] == board[2][1] == "X":
            return True
        elif board[0][2] == board[1][2] == board[2][2] == "X":
            return True
        elif board[0][0] == board[1][1] == board[2][2] == "0":
            return True
        elif board[2][0] == board[1][1] == board[0][2] == "0":
            return True
        elif board[0][0] == board[0][1] == board[0][2] == "0":
            return True
        elif board[1][0] == board[1][1] == board[1][2] == "0":
            return True
        elif board[2][0] == board[2][1] == board[2][2] == "0":
            return True
        elif board[0][0] == board[1][0] == board[2][0] == "0":
            return True
        elif board[0][1] == board[1][1] == board[2][1] == "0":
            return True
        elif board[0][2] == board[1][2] == board[2][2] == "0":
            return True

def StartGameTicTacToe():
    while True:
        if winCheck():
            print("WYGRALES !!! KONIEC GRY")
            break
        gameScheme()

StartGameTicTacToe()



    






