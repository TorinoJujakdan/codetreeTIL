import sys
   
n, m = map(int, sys.stdin.readline().split())

# N이 0보다 큰 동안 반복
while n > 0:
    print(n)
    n //= m  # M으로 나눈 몫으로 N 갱신