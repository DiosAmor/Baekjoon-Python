import sys

n = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(n)]
words = set(words)
words = list(words)
words.sort()
words.sort(key=len)
print(*words,sep="\n")
