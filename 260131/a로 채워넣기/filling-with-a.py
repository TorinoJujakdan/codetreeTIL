word = list(input())
word[1] = 'a'
word[-2] = 'a'

for i in range(len(word)):
    print(word[i], end='')