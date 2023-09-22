#pypy

blank = []
numbers = [list(map(int,input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if numbers[i][j] == 0:
            blank.append([i,j])

def checkRow(x,num):
    for i in range(9):
        if num == numbers[x][i]:
            return False
    return True

def checkCol(y,num):
    for i in range(9):
        if num == numbers[i][y]:
            return False
    return True

def checkRect(x,y,num):
    X = x//3*3
    Y = y//3*3
    for i in range(3):
        for j in range(3):
            if num == numbers[X+i][Y+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):            
            print(*numbers[i], sep=" ")
        exit()
    for num in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x,num) and checkCol(y,num) and checkRect(x,y,num):
            numbers[x][y] = num
            dfs(idx+1)
            numbers[x][y] = 0

dfs(0)