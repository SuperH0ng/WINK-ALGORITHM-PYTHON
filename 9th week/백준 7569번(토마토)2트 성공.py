import copy
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
M, N, H = map(int, input().split())
c = [[input().split() for i in range(N)] for j in range(H)]

queue = deque([])
for i in range(H):
    for j in range(N):
        for l in range(M):
            if c[i][j][l] == '1':
                c[i][j][l] = 0
                queue.append([i, j, l])

while queue:
    p = queue.popleft()
    for i in range(6):
        if p[0] + dx[i] < 0 or p[0] + dx[i] >= len(c) or p[1] + dy[i] < 0 or p[1] + dy[i] >= len(c[0]) or p[2] + dz[i] < 0 or p[2] + dz[i] >= len(c[0][0]):
            continue
        if c[p[0] + dx[i]][p[1] + dy[i]][p[2] + dz[i]] == '0':
            c[p[0] + dx[i]][p[1] + dy[i]][p[2] + dz[i]] = c[p[0]][p[1]][p[2]] + 1
            queue.append([p[0] + dx[i], p[1] + dy[i], p[2] + dz[i]])

loop1, loop2 = True, True
answer = 0
for i in range(H):
    for j in range(N):
        for l in range(M):
            if c[i][j][l] == '0':
                answer = -1
                loop1, loop2 = False, False
                break
            elif int(c[i][j][l]) > answer:
                answer = c[i][j][l]
        if loop2 == False:
            break
    if loop1 == False:
        break

print(answer)


# def ripeTomato(x, y, z):
#     queue = deque([[x, y, z]])
#     global c
#     c = copy.deepcopy(c)
#     c[x][y][z] = 10
#     while queue:
#         p = queue.popleft()
#         for i in range(6):
#             if p[0] + dx[i] < 0 or p[0] + dx[i] >= len(c) or p[1] + dy[i] < 0 or p[1] + dy[i] >= len(c[0]) or p[2] + dz[i] < 0 or p[2] + dz[i] >= len(c[0][0]):
#                 continue
#             if c[p[0] + dx[i]][p[1] + dy[i]][p[2] + dz[i]] == 0:
#                 c[p[0] + dx[i]][p[1] + dy[i]][p[2] +
#                                               dz[i]] = c[p[0]][p[1]][p[2]] + 1
#                 queue.append([p[0] + dx[i], p[1] + dy[i], p[2] + dz[i]])
#             elif c[p[0] + dx[i]][p[1] + dy[i]][p[2] + dz[i]] == 1:
#                 return c[p[0]][p[1]][p[2]] + 1 - 10
#             else:
#                 pass
#     return -1


# def days(H, N, M):
#     answer = 0
#     for i in range(H):
#         for j in range(N):
#             for l in range(M):
#                 if c[i][j][l] == 0:
#                     result = ripeTomato(i, j, l)
#                     if result == -1:
#                         return -1
#                     else:
#                         if result > answer:
#                             answer = result
#     return answer


# print(days(H, N, M))
