a,b,c = map(int,input().split())

if a!=b and b!=c and c!=a:
    print(max(a,b,c)*100)
elif a==b and b!=c:
    print(a*100+1000)
elif a==c and b!=c:
    print(a*100+1000)
elif b==c and b!=a:
    print(b*100+1000)
else:
    print(a*1000+10000)