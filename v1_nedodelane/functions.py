def show_board_simple(board,board_size):
    #print(board,"\n")
    for i in range(1,board_size+1):

        for j in range(1,board_size+1):
            print(board[i][j],end="")
        print()
    
def show_board(board,board_size):
    #nazvy sloupcu
    print("",end="   ")     # odsazeni kvuli nazvum radku
    for k in range(1,board_size+1):
        if k//10!=0:
            print(k//10,end="")
        else:
            print(" ",end="")
    print("\n",end="   ")     # odsazeni kvuli nazvum radku
    for k in range(1,board_size+1):
        print(k%10,end="")
    print()

    for i in range(1,board_size+1):
        #nazvy radku
        if i<10:
            print("",i,end=" ")
        else:   # dvou-ciferne pojmenovani radku
            print(i,end=" ")
        # pole
        for j in range(1,board_size+1):
            print(board[i][j],end="")
        print()

def check_int(x):   # vrati True pokud x je cele cislo
    for digit in x:
        if 48<=ord(digit)<=57:  #ASCII 48-57 je 0-9
            continue
        else:
            return False
    return True

def check_input(x,y,board_size):    
    # vrati True pkud je input v Validni tj. 2 inty oddelene mezerou mezi 1 a board_size, False jinak
    if check_int(x)==True and check_int(y)==True:
        x,y=int(x),int(y)
        if 1<=x<=board_size and 1<=y<=board_size:
            return True
        else:
            print("Zadane policko je mimo hraci plochu, obe souradnice musi byt mezi 1 a",board_size)
            return False
    else:
        print("Vstup musi byt dvojice celych cisel oddelenych mezerou")
        return False

def add_to_active_neighbour(x,y,active,board):    
    # prozkouma vsechny sousedy x,y a udela je aktivni pokud jsou volne "_"
    delta=[[1,1],[1,0],[1,-1],[0,1],[-1,-1],[-1,0],[-1,1],[0,-1]]
    for step in delta:
        X,Y=x+step[0],y+step[1]
        if board[X][Y]=="_" and [X,Y] not in active:
            active.append([X,Y])

def get_mm_active(board,used):
    mm_active=[]
    for el in used:
        add_to_active_neighbour(el[0],el[1],mm_active,board)
    return mm_active