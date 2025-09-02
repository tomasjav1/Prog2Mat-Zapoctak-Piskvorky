board=[[1,1,3,3,1],[1,2,3,4,5],[1,3,1,3,1]]
x=[[1,2],[2,2]]
print(board)

mm_board=[]
for i in board:
    row=[]
    for j in i:
        row.append(j)
    mm_board.append(row)

print(mm_board)

mm_board.pop()
print(board,"\n",mm_board)