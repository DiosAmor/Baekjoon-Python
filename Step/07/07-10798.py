temp = [input() for _ in range(5)]

new_list = ""
for i in range(15):
    for j in range(5):
        if i < len(temp[j]):
            new_list+=(temp[j][i])
print(new_list)