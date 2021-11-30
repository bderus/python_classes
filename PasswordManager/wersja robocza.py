import app

lista = [[1,2,3],[1,2,3],[1,2,3]]
player = input("Wybierz X lub O: ")
if player == "X":
    print("Gracz pierwszy ma X, gracz drugi ma O ")
elif player == "O":
    print("Gracz pierwszy ma O, gracz drugi ma X ")
else:
    print("Nieprawidłowy wybór ")

tabelaGry = input("Wybierz 1, aby rozpocząć grę, wybierz 2, aby wrócić do wyboru menu: ")

if tabelaGry == "1":
    print("Rozpoczyna gracz pierwszy ")
    print("   0  1  2")
    numeracjaPionowa = 0
    for el in lista:
        print(numeracjaPionowa, lista[0])
        numeracjaPionowa += 1
else:
    app.main_menu()

playerOne = input("Wybierz pole(np 1:1, 1:2, 2:2 itd): ")







