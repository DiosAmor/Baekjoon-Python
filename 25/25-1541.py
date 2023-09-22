seq = input()

total = 0
num_str = ''
dic = 0
for i in range(len(seq)):
    if seq[i].isdigit():
        num_str += seq[i]
    else:
        if dic == 1:
            total -= int(num_str)
            num_str = ''
        if dic == 0 and seq[i] == '-':
            dic = 1
            total += int(num_str)
            num_str = ''
        if dic == 0 and seq[i] == '+':
            total += int(num_str)
            num_str = ''
if dic == 1:
    total -= int(num_str)
else:
    total += int(num_str)
print(total)        
        