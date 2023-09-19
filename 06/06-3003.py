chess = [1,1,2,2,2,8]
chess_present = list(input().split())

chess_diff = [chess[i]-int(chess_present[i]) for i in range(0,len(chess))]
for j in range(0,len(chess_diff)):
    print(chess_diff[j],end=" ")