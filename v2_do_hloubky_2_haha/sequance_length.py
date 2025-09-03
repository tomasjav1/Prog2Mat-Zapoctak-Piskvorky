def sequance_len(X,Y,board,board_size):

    charR=board[X][Y] #X nebo O
    def num_in_row(X,Y,k,l):    #pocet stejnych charakteru jako na pozici X,Y  ve smerech (list delky 2) k,l 
        num_in_row=1
        x,y=X,Y
        while 1<=x+k[0]<=board_size and 1<=y+k[1]<=board_size:
            if board[x+k[0]][y+k[1]]==charR:
                num_in_row+=1
                x+=k[0]
                y+=k[1]
            else:
                break
        x,y=X,Y
        while 1<=x+l[0]<=board_size and 1<=y+l[1]<=board_size:
            if board[x+l[0]][y+l[1]]==charR:
                num_in_row+=1
                x+=l[0]
                y+=l[1]
            else:
                break
        return num_in_row


    print("length of sequance of:",charR,"on",X,Y,"in directions:")
    #horizontalni delka -
    horiznotal_length=num_in_row(X,Y,[0,1],[0,-1])
    print(horiznotal_length,"horizontal - ")

    #vertikalni delka |
    vertical_length=num_in_row(X,Y,[1,0],[-1,0])
    print(vertical_length,"vertical | ")

    #diagonalni_1 delka \
    diagonal1_length=num_in_row(X,Y,[1,1],[-1,-1])
    print(diagonal1_length,"diagonal1 \\")

    #diagonalni_2 delka /
    diagonal2_length=num_in_row(X,Y,[1,-1],[-1,1])
    print(diagonal2_length,"diagonal2 /")
    
    goal_len=5
    if horiznotal_length>=goal_len or vertical_length>=goal_len or diagonal1_length>=goal_len or diagonal2_length>=goal_len:
        return True
    else:
        return False
