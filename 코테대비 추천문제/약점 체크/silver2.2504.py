'''
line = list(input())

x = 1
y = 1

answer = 0
bracket = []

for h in range(len(line)):
    i = line[h]
    if i == '(':
        bracket.append('x')
        x *= 2
    elif i == ')':
        if len(bracket) == 0 or bracket[-1] != 'x':
            answer = 0
            break
        elif line[h-1] == '(':
            answer += x * y
            
        bracket.pop()
        x //= 2
    elif i == '[':
        bracket.append('y')
        y *= 3
    elif i == ']':
        if len(bracket) == 0 or bracket[-1] != 'y':
            answer = 0
            break
        elif line[h-1] == '[':
            answer += x * y
        
        bracket.pop()
        y //= 3
        
if bracket:
    answer = 0
print(answer)
'''

I =input()

I = I.replace('()','(1)')
I = I.replace('[]','[1]')

r=''
try:
    for i in I:
        r += {'(':'+2*(', '[':'+3*[', ')':')', ']':'][0]', '1':'1'}[i]
        print(r)
    print(eval(r))
except:
    print(0)