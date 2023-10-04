while (1):
    n = int(input())
    if n == -1:
        break
    else:
        num = []
        total = 0
        for i in range(1,n):
            if n%i==0:
                num.append(i)
                total += i
        if total == n:
            print(n,end=" = 1")
            for j in num[1:]:
                print(" +", j,end="")
            print()
        else:
            print(n,"is NOT perfect.")
