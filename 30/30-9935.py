sen = input()
bomb = input()

bomb_size = len(bomb)
temp = []

for i in range(len(sen)):
    temp.append(sen[i])
    if temp[-1] == bomb[-1]:
        check = 0
        flag = 0
        temp_size = len(temp)
        if temp_size >= bomb_size:
            for j in range(temp_size-bomb_size,temp_size):
                if temp[j] == bomb[check]:
                    check +=1
                else:
                    flag = 1
                    break
            if flag == 0:
                for _ in range(bomb_size):
                    temp.pop()
if len(temp) > 0:
    print("".join(temp))
else:
    print("FRULA")