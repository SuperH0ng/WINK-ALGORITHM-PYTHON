import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
jiyeok = []
check = []

for i in range(N):
    jiyeok.append(list(map(int, input().split())))
    check.append([False] * N)


def countSafeZone(x, y, h, c, j):
    global N
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if c[x][y] == False and j[x][y] > h:
        c[x][y] = True
        countSafeZone(x-1, y, h, c, j)
        countSafeZone(x+1, y, h, c, j)
        countSafeZone(x, y-1, h, c, j)
        countSafeZone(x, y+1, h, c, j)


answer = 0
for height in range(0, 101):
    safeZone = 0
    check = []
    for i in range(N):
        check.append([False] * N)
    for j in range(N):
        for k in range(N):
            if check[j][k] == False and jiyeok[j][k] > height:
                countSafeZone(j, k, height, check, jiyeok)
                safeZone += 1

    if answer < safeZone:
        answer = safeZone
    # print(safeZone)

print(answer)
