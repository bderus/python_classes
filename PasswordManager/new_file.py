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


def gameBoard(player, row=0, column=0):
    if board[row][column] != "X" and board[row][column] != "0":
        print("    0    1    2")

        board[row][column] = player
        if player == "X":
            player = "0"
        elif player == "0":
            player = "X"

        for count, row in enumerate(board):
            print(count, row)

        if winCheck(str(player), board):
            print("win")
            app.main_menu()

        gameScheme(player)
    else:
        print("To pole jest już zajęte ")
        pick_place(player)


def gameScheme(playerChoice):
    pick_place(playerChoice)


def pick_place(playerChoice):
    playerChoicerow = input("Wybierz wiersz: ")
    playerChoicecolumn = input("Wybierz kolumnę: ")

    if (playerChoicerow == "0" or playerChoicerow == "1" or playerChoicerow == "2") and (
            playerChoicecolumn == "0" or "1" or "2"):
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
