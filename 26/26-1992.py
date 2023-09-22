N = int(input())

pic = []
for _ in range(N):
    temp = input()
    temp_list =[]
    for i in range(N):
        temp_list.append(temp[i])
    pic.append(temp_list)
com_pic = []
def com(x,y,N):
    check = 0
    for i in range(x,x+N):
        for j in range(y,y+N):
            if pic[i][j] == "1":
                check +=1
    if check == 0:
        com_pic.append("0")
    elif check == N**2:
        com_pic.append("1")
    else:
        com_pic.append("(")
        com(x,y,N//2)
        com(x,y+N//2,N//2)
        com(x+N//2,y,N//2)
        com(x+N//2,y+N//2,N//2)
        com_pic.append(")")
com(0,0,N)
print("".join(com_pic))