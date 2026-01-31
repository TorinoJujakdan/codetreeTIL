N = int(input())

numbers = list(map(int, input().split()))

for i in range(N):
    numbers[i] *= numbers[i]

print(*numbers)
