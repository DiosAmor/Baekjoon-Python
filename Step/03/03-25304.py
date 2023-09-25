total_money = int(input())
total_number = int(input())
total_money2 = 0
for i in range(0,total_number):
    a,b = map(int,input().split())
    total_money2 += a*b

if total_money == total_money2:
    print("Yes")
else:
    print("No")