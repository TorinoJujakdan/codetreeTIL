n = int(input())
li = list(map(int, input().split()))
li.reverse()


for i in range(len(li)):
    if li[i] % 2 == 0:
        print(li[i], end=" ")
    else:
        continue