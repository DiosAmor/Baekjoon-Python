#pypy

import sys

input = sys.stdin.readline

words = input().strip()
q = int(input())
n = len(words)
dp = [[0]*26 for _ in range(n)]
dp[0][ord(words[0])-97] = 1
for i in range(1,n):
    dp[i][ord(words[i])-97] = 1
    for j in range(26):
        dp[i][j] += dp[i-1][j]
        
for _ in range(q):
    al,l,r = input().split()
    l = int(l)
    r = int(r)
    al_index = ord(al)-97
    if l > 0:
        print(dp[r][al_index]-dp[l-1][al_index])
    else:
        print(dp[r][al_index])