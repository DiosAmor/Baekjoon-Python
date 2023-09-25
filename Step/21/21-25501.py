def recursion(words,l,r):
    if l>=r:
        return [1,l+1]
    elif words[l] != words[r]:
        return [0,l+1]
    else: return recursion(words,l+1,r-1)
    
T = int(input())

for _ in range(T):
    words = input()
    result, num = recursion(words,0,len(words)-1)
    print("{} {}".format(result, num))