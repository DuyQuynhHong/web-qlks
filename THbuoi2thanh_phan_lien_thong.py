n,m,k = [int(x) for x in input().split()]
a = []
for i in range(n+1):
    a.append([])
b = [0] * (n+1)
for i in range(m):
    x,y = [int(x) for x in input().split()]
    a[x].append(y)
    a[y].append(x)
c = []
c.append(k)
b[k] = 1
while len(c) > 0:
    x = c.pop()
    for i in a[x]:
        if b[i] == 0 :
            c.append(i)
            b[i] = 1 
for i in range(1,n+1):
    if b[i] == 0 :
        print(i)