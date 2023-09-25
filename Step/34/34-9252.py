word1 = input()
word2 = input()
dp = [[""]*(len(word1)+1) for _ in range(len(word2)+1)]

for i in range(1,len(word2)+1):
    for j in range(1,len(word1)+1):
        if word1[j-1] == word2[i-1]:
            dp[i][j] = dp[i-1][j-1] + word1[j-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
result = dp[-1][-1]
print(len(result))
print(result)