n= int(input())
memo = [1,2]
result = 0
if n == 1 or n == 2:
    result = memo[n-1]
else:
    for i in range(3,n+1):
        temp = memo[0] + memo[1]
        if temp >= 15746:
            memo.append(temp%15746)
        else:
            memo.append(temp)
        memo = memo[1:3]
    result = memo[1]
print(result)