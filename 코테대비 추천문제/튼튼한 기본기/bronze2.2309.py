s = []
for _ in range(9):
    s.append(int(input()))

sub = sum(s) - 100
for i in range(8):
    for j in range(i+1,9):
        if sub == s[i]+s[j]:
            a = s[i]
            b = s[j]
            s.remove(a)
            s.remove(b)
            s.sort()
            print(*s, sep='\n')
            exit()


