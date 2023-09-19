n = int(input())
XY = [[False]*100 for _ in range(100)]

for _ in range(n):
    X,Y = map(int,input().split())
    for i in range(X-1,X+9):
        for j in range(Y-1,Y+9):
            XY[i][j] = True
result = 0
for i in range(100):
    for j in range(100):
        if XY[i][j]:
            result += 1
print(result)