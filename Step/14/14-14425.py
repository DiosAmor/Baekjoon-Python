N,M = map(int,input().split())
S = [input() for _ in range(N)]
Words = [input() for _ in range(M)]

S = set(S)
Words2 = set(Words)
Same = Words2 & S

count_num=0
for i in Same:
    count_num+=Words.count(i)
print(count_num)