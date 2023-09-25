word = input()

words = []
for i in range(len(word)):
    for j in range(len(word)):
        if i+j<=len(word):
            words.append(word[i:i+j])
words = set(words)
print(len(words))