case = int(input())
temp=[]
for i in range(0,case):
    a,b = map(int,input().split())
    temp.append(a+b)
for i in range(0,len(temp)):
    print("Case #{}: {}".format(i+1,temp[i]))