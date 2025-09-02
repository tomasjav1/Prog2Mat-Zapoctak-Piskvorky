import random as ran
from functions import show_board
from functions import check_input
from functions import add_to_active_neighbour

board_size=15       # 5<  <100, idealne liche
board=[["_" for i in range(board_size+2)] for i in range(board_size+2)]         
for i in range(board_size+2):   #hraci pole cislovane on 1 do board_size s okrajem #
    board[0][i]="#"
    board[i][0]="#"
    board[board_size+1][i]="#"
    board[i][board_size+1]="#"
#  _ empty space
#  # obstacle
#  X cross
#  O nought

used=[]     # obsazena policka O nebo X
active=[]   # neobsazene (tj. je na nich "_") policka ktera soudeni s obsazenimy


#TODO REMOVE #
## 1.radek
#print("Chcete hrat s prekazkami? '1' pro Ano, '0'  pro Ne")
#if int(input())==1:
#    for i in range(board_size//2):
#        x,y=ran.randint(2,board_size-1),ran.randint(2,board_size-1)
#        board[x][y]="#"
#    print("Zde jsou nahodne vygenerovane prekazky:")
#    show_board(board)
#    obstacles=True
#else:
#   obstacles=False 
obstacles=False     #REMOVE


#TODO REMOVE #
##2.radek
#print("Chcete zacinat? '1' pro Ano, '0' pro Ne")
#if int(input())==1:
#    player_starts=True
#else:
#    player_starts=False
player_starts=True  #REMOVE

##TODO REMOVE #
##3.radek
#print("Jake chcete uvodni rozlozeni krouzku/krizku? '1' pro 3 nahodne (z toho ma pouze jednu zacinajici hrac), '0' pro zadne, '-1' pro vlastni")
#def ran_empry_space(board):
#    x,y=ran.randint(2,board_size-1),ran.randint(2,board_size-1)
#    while board[x][y]!="_":
#        x,y=ran.randint(2,board_size-1),ran.randint(2,board_size-1)
#    return x,y
#
#inp3=int(input())
#if inp3==1:  #nahodne
#    x,y=ran_empry_space(board)
#    board[x][y]="O"
#    used.append([x,y])
#    x,y=ran_empry_space(board)
#    board[x][y]="X"
#    used.append([x,y])
#    x,y=ran_empry_space(board)
#    if player_starts==False:
#        board[x][y]="O"
#    else:
#        board[x][y]="X"
#    used.append([x,y])
#
#elif inp3==-1:   #vlastni
#    #noughts O
#    print("Zadejte souradnice kolecek 'O' oddelenych mezerou, zadejte '-1' pro ukonceni ")
#    inp=input()
#    while inp!="-1":
#        x,y=inp.split()
#        if check_input(x,y,board_size)==True:
#           x,y=int(x),int(y)
#           if board[x][y]=="_":
#               board[x][y]="O"
#               used.append([x,y])
#           else:
#               print("Uvedene policko je jiz obsazene, vyberte jine")
#               show_board(board,board_size)
#        inp=input()
#    #crosses X
#    print("Zadejte souradnice krizku 'X' oddelenych mezerou, zadejte '-1' pro ukonceni ")
#    inp=input()
#    while inp!="-1":
#        x,y=inp.split()
#        if check_input(x,y,board_size)==True:
#           x,y=int(x),int(y)
#           if board[x][y]=="_":
#               board[x][y]="X"
#               used.append([x,y])
#           else:
#               print("Uvedene policko je jiz obsazene, vyberte jine")
#               show_board(board,board_size)
#        inp=input()


# TODO DODELAT startovni aktivni policka kdyz zacina pocitac, i se zavislosti na inp3 tj. zacinajici rozlozeni
#if player_starts==False:    # zacina pocitac, nyni urcim zacinajici tah
#    if obstacles==False:    #bez prekazek, zacinam ve stredu
#    
#    else:   # s prekazkami, zacimam co nejvic ve predu tak abych nesousedil s prekazkami


print("=================")
print("Uvodni hraci pole")
print("=================")
show_board(board,board_size)

# TODO kontrola vstupu i kontrola splitu ve vstupu
# TODO aktivni policka ve input3