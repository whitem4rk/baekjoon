small = int(input()) 
big = int(input())

primelist = list(range(2,big+1))
for i in range(2,big+1):
    for j in range(2,big+1):
        if i*j > big+1:
            break
        elif  primelist.count(i*j) != 0:
            primelist.remove(i*j)

primelist = list(filter(lambda x: x>=small, primelist))
if len(primelist)==0:
    print(-1)
else:
    print(sum(primelist))
    print(primelist[0])
    
    
# best code
'''
a = [True] * 10001
a[0] = False
a[1] = False
for i in range(10001):
    if a[i]:
        j = 2 * i
        while j <= 10000:
            a[j] = False
            j += i
m = int(input())
n = int(input())
b = []
for i in range(m, n + 1):
    if a[i]:
        b.append(i)
if len(b) == 0:
    print(-1)
else:
    print(sum(b))
    print(b[0])
'''