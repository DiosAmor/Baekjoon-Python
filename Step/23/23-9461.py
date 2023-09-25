P = [1,1,1,2,2]
for i in range(5,100):
    temp = P[i-1]+P[i-5]
    P.append(temp)
T = int(input())
for _ in range(T):
    print(P[int(input())-1])
    