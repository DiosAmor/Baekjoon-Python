temp=[]
while 1:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        temp.append(a+b)
for i in range(0,len(temp)):
    print(temp[i])