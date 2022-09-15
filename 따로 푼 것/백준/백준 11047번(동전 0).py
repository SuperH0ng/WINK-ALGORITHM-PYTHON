import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0
coin = [int(input()) for _ in range(n)]

for i in range(n-1, -1, -1) :
    tmp = coin[i]
    if k >= tmp :
        c = k // tmp
        k -= c * tmp
        answer += c

print(answer)