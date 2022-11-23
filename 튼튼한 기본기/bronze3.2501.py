n, k= map(int, input().split(' '))

index = 0
for i in range(1,n+1):
    if n % i == 0:
        index += 1
    
    if index == k:
        print(i)
        break

if index < k:
    print(0)