humanlist = [0,]
for _ in range(10):
    n1, n2 = map(int, input().split())
    humanlist.append(humanlist[-1]+(n2-n1))
print(max(humanlist))