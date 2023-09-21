number = int(input())

def fi(num):
    if 0<=num and num <= 1:
        return num
    else:
        return fi(num-1)+fi(num-2)
print(fi(number))