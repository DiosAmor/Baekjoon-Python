sen = input()
check = 0
for i in range(int(len(sen)/2)):
    if sen[i] != sen[-(i+1)]:
        print(0)
        check = 1
        break
if check == 0:
    print(1)
    