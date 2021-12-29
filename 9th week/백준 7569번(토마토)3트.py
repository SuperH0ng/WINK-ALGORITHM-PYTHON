from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
M, N, H = map(int, input().split())
c = [[input().split() for i in range(N)] for j in range(H)]

queue = deque([])
checkList = []
for i in range(H):
    for j in range(N):
        for l in range(M):
            if c[i][j][l] == '1':
                c[i][j][l] = 0
                queue.append([i, j, l])
            elif c[i][j][l] == '0':
                checkList.append([i, j, l])

answer = 0
while queue:
    p = queue.popleft()
    for i in range(6):
        if p[0] + dx[i] < 0 or p[0] + dx[i] >= len(c) or p[1] + dy[i] < 0 or p[1] + dy[i] >= len(c[0]) or p[2] + dz[i] < 0 or p[2] + dz[i] >= len(c[0][0]):
            continue
        if c[p[0] + dx[i]][p[1] + dy[i]][p[2] + dz[i]] == '0':
            c[p[0] + dx[i]][p[1] + dy[i]][p[2] + dz[i]] = c[p[0]][p[1]][p[2]] + 1
            answer = c[p[0]][p[1]][p[2]] + 1
            queue.append([p[0] + dx[i], p[1] + dy[i], p[2] + dz[i]])

for z in checkList:
    if c[z[0]][z[1]][z[2]] == '0':
        answer = -1
        break

print(answer)
