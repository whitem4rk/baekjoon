S = int(input())

i = 2
sum = 1
while True:
    sum += i
    if sum > S:
        print(i-1)
        exit()
    i += 1