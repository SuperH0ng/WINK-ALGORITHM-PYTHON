import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())
maze = [input() for i in range(M)]
countList = [[-1] * N for _ in range(M)]
countList[0][0] = 0
queue = deque([[0,0]])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue :
    x, y = queue.popleft()
    for i in range(4) :
        if x + dx[i] < 0 or x + dx[i] >= M or y + dy[i] < 0 or y + dy[i] >= N:
            continue
        if countList[x + dx[i]][y + dy[i]] != -1 :
            continue
        if maze[x + dx[i]][y + dy[i]] == '0' :
            queue.appendleft([x + dx[i], y + dy[i]])
            countList[x + dx[i]][y + dy[i]] = countList[x][y]
        else :
            queue.append([x + dx[i], y + dy[i]])
            countList[x + dx[i]][y + dy[i]] = countList[x][y] + 1

print(countList[M-1][N-1])