N = int(input())
number = N

for _ in range(N):
    word = input()
    temp = [word[0]]
    for i in range(1,len(word)):
        if word[i] != temp[-1]:
            if temp.count(word[i]) != 0:
                number -= 1
                break
            else:
                temp.append(word[i])
print(number)