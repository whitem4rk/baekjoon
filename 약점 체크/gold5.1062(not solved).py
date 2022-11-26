# 1<=N=50
# 0<=K<=26
# 8<= 단어길이 <=15  
# 소문자만, 단어중복 X

#a n t i c

N, K = map(int, input().split())
wordlist = []
for _ in range(N):
    word = input()
    wordlist.append(word[4:-4])

print(wordlist)
spell_count = 5

