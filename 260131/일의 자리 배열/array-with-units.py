a, b = map(int, input().split())
li = [a, b]
i = 0
while True:
    newnum = (li[i] + li[i + 1]) % 10
    li.append(newnum)
    i += 1
    if i == 8:
        break
print(*li) 