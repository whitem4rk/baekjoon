# My code
'''
T = int(input())

for i in range(T):
    n = int(input())  # n >= 1

    binlist = []
    for j in range(1000001):
        mod = n % 2
        n = int(n/2)
        
        if mod == 1:
            binlist.append(str(j))
        
        if n == 0:
            break
    
    print(' '.join(binlist))
'''

# Better code
T = int(input())

for i in range(T):
    n = bin(int(input()))[2:]
    for j in range(len(n)):
        if n[-j-1] == '1':
            print(j, end=' ')
    
