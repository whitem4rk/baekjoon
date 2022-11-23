T = int(input())

num = list(map(int, input().split()))
prime = 0

for i in num:
    if i == 1:
        continue
    prime += 1
    for j in range(2, i):
        if i % j == 0:
            prime -= 1
            break

print(prime)