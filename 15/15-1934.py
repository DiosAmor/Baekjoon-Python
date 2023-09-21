case = int(input())

for _ in range(case):
    a,b = map(int,input().split())
    num_a = {1,a}
    num_b = {1,b}
    for i in range(2,a//2):
        if a%i==0:
            num_a.add(i)
            num_a.add(a//i)
    for j in range(2,b//2):
        if b%j==0:
            num_b.add(j)
            num_b.add(b//j)
    GCD = max(num_a&num_b)
    LCM = int(a*b/GCD)
    print(LCM)