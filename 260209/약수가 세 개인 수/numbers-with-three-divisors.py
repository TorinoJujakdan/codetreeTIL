start, end = map(int, input().split())

# Please write your code here.
count = 0
for i in range(start, end + 1):
    d_count = 0
    for d in range(1, i + 1):
        if i % d == 0:
            d_count += 1
    if d_count == 3:
        count += 1
print(count)