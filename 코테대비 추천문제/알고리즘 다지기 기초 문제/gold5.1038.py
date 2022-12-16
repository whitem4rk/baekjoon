# combination
'''
from itertools import combinations

n = int(input())
nums = list() 

for i in range(1, 11):     
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)                    
        nums.append(int("".join(map(str, comb))))

nums.sort()  

try:
    print(nums[n])
except:    
    print(-1)
'''

# recursive
n = int(input())
ans = []

def decrease(x):
    ans.append(x)
    left = int(str(x)[0])
    for i in range(left+1, 10):
        decrease(int(str(i) + str(x)))

for i in range(10):
    decrease(i)
    
ans.sort()

try :
    print(ans[n])
except : 
    print(-1)