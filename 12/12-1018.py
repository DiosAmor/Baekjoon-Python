candidate1 = [["W","B"]*4,["B","W"]*4]*4
candidate2 = [["B","W"]*4,["W","B"]*4]*4

N, M = map(int,input().split())

origin = [input() for _ in range(N)]

result = 8*8

for i in range(N-7):
    for j in range(M-7):
        diff_1=0
        diff_2=0
        for k in range(8):
            for l in range(8):
                if origin[i+k][j+l] != candidate1[k][l]:
                    diff_1+=1
                if origin[i+k][j+l] != candidate2[k][l]:
                    diff_2+=1
        if result > diff_1:
            result = diff_1
        if result > diff_2:
            result = diff_2
print(result)