T = int(input())
for _ in range(T):
    mon = int(input())
    for i in [25,10,5,1]:
        print(mon//i,end=" ")
        mon = mon%i
    print()
