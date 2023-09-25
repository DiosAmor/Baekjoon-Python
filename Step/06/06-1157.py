words = input().lower()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
al_count=[]
for i in range(0,len(alphabet)):
    al_count.append(words.count(alphabet[i]))
if al_count.count(max(al_count))==1:
    print(alphabet[al_count.index(max(al_count))].upper())
else:
    print("?")

