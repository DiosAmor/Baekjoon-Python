num = int(input())

check = 0
for i in range(1,num):
    i_str = str(i)
    to = i
    for j in range(0,len(i_str)):
        to += int(i_str[j])
    if to == num:
        print(i)
        check = 1
        break
if check == 0:
    print(0)