temp=[]
while 1:
    try:
        a,b = map(int,input().split())
        temp.append(a+b)
    except:
        break
for i in range(0,len(temp)):
    print(temp[i])