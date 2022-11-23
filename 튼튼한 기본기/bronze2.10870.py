from functools import reduce
n = int(input())
fib = lambda n:reduce(  lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1]  )[0]
print(fib(n))