# python3 시간초과
'''
from itertools import permutations

num_count = int(input())
numlist = list(map(int, input().split()))
opt = ['+','-','*','//']
opt_count = list(map(int, input().split()))
opt_list = []

for i in range(len(opt)):
    for j in range(opt_count[i]):
        opt_list.append(opt[i])

maxi = -1e9
mini = 1e9

for case in permutations(opt_list, len(opt_list)):
    total = numlist[0]
    for x in range(1, len(numlist)):
        if case[x-1] == '+':
            total += numlist[x]
        elif case[x-1] == '-':
            total -= numlist[x]
        elif case[x-1] == '*':
            total *= numlist[x]
        elif case[x-1] == '//':
            total = int(total/numlist[x])
        
    maxi = max(maxi, total)
    mini = min(mini, total)
        
print(maxi)
print(mini)
'''

num_count = int(input())
numlist = list(map(int, input().split()))
opt_count = list(map(int, input().split()))
maxi = -1e9
mini = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global mini, maxi
    if depth == num_count:
        maxi = max(total,maxi)
        mini = min(total,mini)
        return
    
    if plus:
        dfs(depth+1, total + numlist[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - numlist[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * numlist[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / numlist[depth]), plus, minus, multiply, divide-1)
        
dfs(1,numlist[0],opt_count[0],opt_count[1],opt_count[2],opt_count[3])
print(maxi)
print(mini)