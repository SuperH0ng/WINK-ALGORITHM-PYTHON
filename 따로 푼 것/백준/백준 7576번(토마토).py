from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
tomato = [list(map(int, input().strip().split())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque([])
checkList = []
answer = 1

for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1 :
            queue.append([i,j])
        elif tomato[i][j] == 0 :
            checkList.append([i, j])

while queue :
    p = queue.popleft()
    for i in range(4) :
        nn = p[0] + dx[i]
        mm = p[1] + dy[i]
        if nn < 0 or nn >= n or mm < 0 or mm >= m :
            continue
        if tomato[nn][mm] == 0 :
            answer = tomato[p[0]][p[1]] + 1
            tomato[nn][mm] = answer
            queue.append([nn,mm])

answer -= 1

for c in checkList :
    if tomato[c[0]][c[1]] == 0 :
        answer = -1
        break

print(answer)
