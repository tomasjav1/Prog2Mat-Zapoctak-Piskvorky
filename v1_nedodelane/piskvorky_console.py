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

import sys


#SAM PROTI SOBE
print("\nGAME STARTS \n")
O_turn=player_starts
print("Zadejte souradnice dalsiho tahu: radek mezera sloupec. Na tahu je ",end="")
if O_turn==True:
    print("O")
else:
    print("X")
 
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