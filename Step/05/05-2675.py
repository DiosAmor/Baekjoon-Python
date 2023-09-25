case = int(input())

for i in range(0,case):
    R,S=map(str,input().split())
    for j in range(0,len(S)):
        print(S[j]*int(R),end="")
    print()