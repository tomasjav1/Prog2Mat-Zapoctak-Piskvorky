import board_setup  #zaroven ho spusti
from board_setup import player_starts
from board_setup import board_size
from board_setup import board
from board_setup import used
from board_setup import active
from functions import show_board
from functions import check_input
from functions import add_to_active_neighbour
from utility_function import utility
from minimax_f import minimax

import time
import sys




print("\nGAME STARTS \n")
O_turn=player_starts
print("Zadejte souradnice dalsiho tahu: radek mezera sloupec. Na tahu je ",end="")
if O_turn==True:
    print("O")
else:
    print("X")

#SAM PROTI SOBE
def duo(O_turn): 
    inp=input()
    while inp!="-1":
        x,y=inp.split()
        #TODO zkokntrolovat spit tj zda je ve stringu mezera
        if check_input(x,y,board_size)==True:
            x,y=int(x),int(y)
            if board[x][y]=="_":
                used.append([x,y])
                if O_turn==True:
                    board[x][y]="O"
                    O_turn=False
                else:
                    board[x][y]="X"
                    O_turn=True

                if [x,y] in active:
                    active.remove([x,y])
                add_to_active_neighbour(x,y,active,board)
                print("AKTIVNI POLICKA:",len(active))

                score=utility(board,used)
                print("SCORE:",score)
                print()
                if abs(score)>=900000:   # konec
                    show_board(board,board_size)
                    if O_turn==True:    # je prohozene po tahu
                        print("X wins")
                    else:
                        print("O wins")

                    sys.exit()
                show_board(board,board_size)

            else:
                show_board(board,board_size)
                print("Uvedene policko je jiz obsazene, vyberte jine")


        print("Zadejte souradnice dalsiho tahu: radek mezera sloupec. Na tahu je ",end="")
        if O_turn==True:
            print("O")
        else:
            print("X")

        inp=input()
#duo(O_turn)

#PROTI POCITACI
# kde zacina hrac
#TODO muze zacinat i Minimax
def solo():
    inp=input()
    while inp!="-1":
        # tah hrace
        x,y=inp.split()
        #TODO zkokntrolovat spit tj zda je ve stringu mezera
        if check_input(x,y,board_size)==True:
            x,y=int(x),int(y)
            if board[x][y]=="_":
                used.append([x,y])
                board[x][y]="O"

                if [x,y] in active:
                    active.remove([x,y])
                add_to_active_neighbour(x,y,active,board)
                print("AKTIVNI POLICKA:",len(active))

                score=utility(board,used)
                print("SCORE:",score)
                print()
                if abs(score)>=900000:   # konec
                    show_board(board,board_size)
                    print("O wins")
                    sys.exit()
                show_board(board,board_size)

            else:   #board[x][y]== "obsazene policko"
                show_board(board,board_size)
                print("Uvedene policko je jiz obsazene, vyberte jine")
                print("Zadejte souradnice dalsiho tahu: radek mezera sloupec. Na tahu je O")
                inp=input()
                continue
        else:
            print("Zadejte souradnice dalsiho tahu: radek mezera sloupec. Na tahu je O")
            inp=input()
            continue

        #delay 0.3s
        time.sleep(0.3)
        
        # tah minimaxu
        move=minimax(board,used,2,False)
        print(move)
        if board[move[0]][move[1]]=="_":
            board[move[0]][move[1]]="X"
            used.append(move)
            if move in active:
                active.remove(move)
            add_to_active_neighbour(move[0],move[1],active,board)
            print("AKTIVNI POLICKA:",len(active))

            score=utility(board,used)
            print("SCORE:",score)
            print()
            if abs(score)>=900000:   # konec
                    show_board(board,board_size)
                    print("X wins")
                    sys.exit()
            show_board(board,board_size)
        else:
            print("minimax se snazi tahnout na obsazene policko")
            print("tah",move[0],move[1])
            print("char tam kam chce hrat",board[move[0]][move[1]])

        #input hrace
        print("Zadejte souradnice dalsiho tahu: radek mezera sloupec. Na tahu je O")
        inp=input()
solo()


# TODO budu prozkoumavat tahy do minimaxu jen z aktivnich (sousednich) policek,
#  pokud zadne neni (1.tah) je automaticky veprostred
#  i do board_setup dat aktivni policka

#def showBooleanBoard(board):
#    for i in range(1,boardS+1):
#        for j in range(1,boardS+1):
#            if board[i][j]==True:
#                print(1,end="")
#            else:
#                print(0,end="")
#        print()



# python piskvorky_console.py
# Get-content input.txt | python piskvorky_console.py