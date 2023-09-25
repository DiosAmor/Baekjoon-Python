n = int(input())

In = set()

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        In.add(name)
    if state == "leave":
        In.discard(name)
In = list(In)
In.sort(reverse=True)
for i in range(len(In)):
    print(In[i])