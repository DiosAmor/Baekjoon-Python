number = int(input())
users = [input().split() for _ in range(number)]

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    mer_arr=[]
    l=h=0
    while l < len(low_arr) and h <len(high_arr):
        if int(low_arr[l][0]) <= int(high_arr[h][0]):
            mer_arr.append(low_arr[l])
            l+=1
        else:
            mer_arr.append(high_arr[h])
            h+=1
    mer_arr += low_arr[l:]
    mer_arr += high_arr[h:]
    return mer_arr

users = merge_sort(users)
for i in range(len(users)):
    print(" ".join(users[i]))