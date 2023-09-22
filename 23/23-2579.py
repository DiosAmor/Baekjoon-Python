n = int(input())
score = [0]*n
stair = [0]*n
for i in range(n):
    stair[i] = int(input())
    if i == 0:
        score[i] = stair[i]
    elif i == 1:
        score[i] = stair[i]+stair[i-1]
    elif i == 2:
        score[i] = max(stair[i]+stair[i-2],stair[i]+stair[i-1])
    else:
        temp2 = score[i-2] + stair[i]
        temp3 = score[i-3] + stair[i-1] + stair[i]
        score[i] = max(temp2,temp3)
print(score[n-1])