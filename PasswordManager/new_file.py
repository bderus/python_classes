import app

board = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]
print("    0    1    2")

for count, row in enumerate(board):
    print(count, row)


def winCheck(playerChoice, board):
    if board[0][0] == board[1][1] == board[2][2] == playerChoice:
        return True
    elif board[2][0] == board[1][1] == board[0][2] == playerChoice:
        return True
    elif board[0][0] == board[0][1] == board[0][2] == playerChoice:
        return True
    elif board[1][0] == board[1][1] == board[1][2] == playerChoice:
        return True
    elif board[2][0] == board[2][1] == board[2][2] == playerChoice:
        return True
    elif board[0][0] == board[1][0] == board[2][0] == playerChoice:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == playerChoice:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == playerChoice:
        return True

def drawCheck(board):
    for row in board:
        for element in row:
            if element == "*":
                return False

    return True

""" if board[0][0] != "*" and board[0][1] != "*" and board[0][2] != "*" and board[1][0] != "*" and \
            board[1][1] != "*" and board[1][2] != "*" and board[2][0] != "*" and \
            board[2][1] != "*" and board[2][2] != "*":
        return True"""

def gameBoard(playerChoice, playerChoicerow, playerChoicecolumn):
    if board[playerChoicerow][playerChoicecolumn] != "X" and board[playerChoicerow][playerChoicecolumn] != "0":
        print("    0    1    2")

        board[playerChoicerow][playerChoicecolumn] = playerChoice


        for count, row in enumerate(board):
            print(count, row)

        if winCheck(str(playerChoice), board):
            print("WIN")
            app.main_menu()

        if drawCheck(board):
            print("DRAW")
            app.main_menu()

        if playerChoice == "X":
            playerChoice = "0"
        elif playerChoice == "0":
            playerChoice = "X"

        gameScheme(playerChoice)
    else:
        print("To pole jest już zajęte ")
        pick_place(playerChoice)


def gameScheme(playerChoice):
    pick_place(playerChoice)


def pick_place(playerChoice):
    playerChoicerow = input("Wybierz wiersz: ")
    playerChoicecolumn = input("Wybierz kolumnę: ")

    if (playerChoicerow == "0" or playerChoicerow == "1" or playerChoicerow == "2") and (
            playerChoicecolumn == "0" or playerChoicecolumn == "1" or playerChoicecolumn == "2"):
        gameBoard(str(playerChoice), int(playerChoicerow), int(playerChoicecolumn))
    else:
        pick_place(playerChoice)


def StartGameTicTacToe():
    playerChoice = input("Wybierz X lub O: ")
    if playerChoice == "X" or playerChoice == "0":
        gameScheme(playerChoice)
    else:
        StartGameTicTacToe()


StartGameTicTacToe()
