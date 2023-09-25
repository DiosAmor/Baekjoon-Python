num = int(input())
i=0
number =665
while i<num:
    number +=1
    temp = str(number)
    for j in range(len(temp)-2):
        if temp[j:j+3] == "666":
            i+=1
            break
print(number)