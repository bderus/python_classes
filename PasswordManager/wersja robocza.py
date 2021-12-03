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

while True:
    playerChoice = input("Wybierz X lub O: ")
    playerChoicerow = input("Wybierz wiersz: ")
    playerChoicecolumn = input("Wybierz kolumnę: ")

    if gameBoard(playerChoice,int(playerChoicerow),int(playerChoicecolumn)):
        print(board)
    






