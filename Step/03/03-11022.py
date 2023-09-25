case = int(input())
temp=[]
temp2=[]
for i in range(0,case):
    a,b = map(int,input().split())
    temp2.append([a,b])
    temp.append(a+b)
for i in range(0,len(temp)):
    print("Case #{}: {} + {} = {}".format(i+1,temp2[i][0],temp2[i][1],temp[i]))