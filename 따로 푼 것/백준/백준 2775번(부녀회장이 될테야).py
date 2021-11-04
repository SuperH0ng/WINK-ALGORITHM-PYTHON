import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    residents = [x+1 for x in range(n)]

    if n == 1:
        break

    for j in range(k):
        for l in range(1, n):
            residents[l] += residents[l-1]

    print(residents[-1])
