arr_check = []
def merge_sort(arr,arr_check):
    if len(arr)<2:
        return [arr, arr_check]
    mid = len(arr)//2+len(arr)%2
    low_arr, arr_check = merge_sort(arr[:mid],arr_check)
    high_arr, arr_check = merge_sort(arr[mid:],arr_check)
    
    merged_arr=[]
    l=h=0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            arr_check.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            arr_check.append(high_arr[h])
            h+=1
    merged_arr += low_arr[l:]
    arr_check += low_arr[l:]
    merged_arr += high_arr[h:]
    arr_check += high_arr[h:]
    return [merged_arr, arr_check]

N,K = map(int,input().split())
array = list(map(int,input().split()))
merge, arr_check = merge_sort(array,[])

if len(arr_check)<K:
    print(-1)
else:
    print(arr_check[K-1])