big ,small = map(int, input().split())

if big < small:
    big ,small = small, big

def gcd(a,b):
    while True:
        n = a % b
        if n == 0:
            return b
        else:
            a, b = b, n
            

g = gcd(big,small)
l = big * small // g

print(g)
print(l)