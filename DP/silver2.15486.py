n = int(input())
d = [0 for _ in range(n+2)]
day = [0]
value = [0]
for i in range(n):
    a,b = map(int,input().split())
    day.append(a)
    value.append(b)

for i in range(1,n+1) :
    if d[i] < d[i-1]:
        d[i] = d[i-1]
        print(f'd[{i}] = d[{i-1}]')
    if i + day[i] <= n+1 :
        if d[i + day[i]] < d[i] + value[i] :
            d[i + day[i]] = d[i] + value[i]
            print(f'd[{i} + day[{i}] = d[{i}] + value[{i}]')

print(max(d))