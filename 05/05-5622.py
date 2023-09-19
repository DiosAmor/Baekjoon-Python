words = input()

time =0
for i in range(0,len(words)):
    if words[i] == 'A' or words[i] == 'B' or words[i] == 'C':
        time += 3
    elif words[i] == 'D' or words[i] == 'E' or words[i] == 'F':
        time += 4
    elif words[i] == 'G' or words[i] == 'H' or words[i] == 'I':
        time += 5
    elif words[i] == 'J' or words[i] == 'K' or words[i] == 'L':
        time += 6
    elif words[i] == 'M' or words[i] == 'N' or words[i] == 'O':
        time += 7
    elif words[i] == 'P' or words[i] == 'Q' or words[i] == 'R' or words[i] == 'S':
        time += 8
    elif words[i] == 'T' or words[i] == 'U' or words[i] == 'V':
        time += 9
    elif words[i] == 'W' or words[i] == 'X' or words[i] == 'Y' or words[i] == 'Z':
        time += 10
print(time)