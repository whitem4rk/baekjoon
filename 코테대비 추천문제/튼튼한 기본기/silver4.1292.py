x ,y = map(int,input().split())

a = '0'
for i in range(1,50):
    a += (','+str(i))*i

numlist = a.split(',')
numlist = list(map(int, numlist))
numlist = numlist[x:y+1]
print(sum(numlist))

