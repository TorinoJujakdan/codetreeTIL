N = int(input())
count = 1
for i in range(N):
    for j in range(i + 1):
        print(count, end =' ')
        count += 1
    print()