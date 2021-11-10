import sys
input = sys.stdin.readline

N, K = map(int, input().split())

baeYeol = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1) :
    W, V = map(int, input().split())

    for j in range(1, K+1):
        
        if j>= W :
            baeYeol[i][j] = max(baeYeol[i-1][j], baeYeol[i-1][j-W] + V)
        else :
            baeYeol[i][j] = baeYeol[i-1][j]
for i in baeYeol:
    print(i)
print(baeYeol[-1][-1])