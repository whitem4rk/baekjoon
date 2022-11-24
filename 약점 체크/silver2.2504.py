'''
import sys 
line = list(input())

x = 1
y = 1

answer = 0
bracket = []
started = True
error = False

for i in line:
    if i == '(':
        bracket.append('x')
        started = True
        x *= 2
    elif i == ')':
        if bracket[-1] == 'x':
            bracket.pop()
        else:
            error = True
            
        if started:
            answer += x * y
            started = False
        x //= 2
    elif i == '[':
        bracket.append('y')
        started = True
        y *= 3
    elif i == ']':
        if bracket[-1] == 'y':
            bracket.pop()
        else:
            error = True
        if started:
            answer += x * y
            started = False
        y //= 3
        
if error:
    print(0)
else:
    print(answer)
'''



def solve(l):
	if len(l) == 0 : return 1
	dic = {'(':')', '[':']'}
	val, sub, stk = 0, '', []
	
	for i in l:
		sub += i
		if len(stk) > 0 and dic.get(stk[-1], '') == i : stk.pop()
		else : stk.append(i)
		
		if len(stk) == 0:
			val += solve(sub[1:-1]) * (2 if sub[0] == '(' else 3)
			sub = ''
			
	if len(stk) > 0 : return 0
	return val

print(solve(input()))