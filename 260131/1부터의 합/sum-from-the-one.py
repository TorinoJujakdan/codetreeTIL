n = int(input())

ans = 0
for i in range(1, 101):
    if ans < n:
        ans += i
        continue
    elif ans >= n:
        print(i - 1)
        break
