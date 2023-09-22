N = int(input())
A = list(map(int,input().split()))

result = [A[0]]
for i in A[1:]:
    if result[-1] < i:
        result.append(i)
    else:
        start = 0
        end = len(result)
        while start <= end:
            mid = (start+end)//2
            if result[mid] >= i:
                end = mid - 1
            else:
                start = mid + 1
        result[start] = i
print(len(result))