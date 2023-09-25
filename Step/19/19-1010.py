def com(M,N):
    temp_up = 1
    for i in range(N):
        temp_up *= M
        M -= 1
    temp_under = 1
    for j in range(1,N+1):
        temp_under *= j
    return temp_up//temp_under

case = int(input())
for _ in range(case):
    N,M = map(int,input().split())
    print(com(M,N))
