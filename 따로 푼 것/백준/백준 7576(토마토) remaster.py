from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

tomato = list(list(map(int, input().split())) for i in range(n))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque([])

for y in range(n) :
    for x in range(m) :
         if tomato[y][x] == 1 :
            q.append(y); q.append(x)
            
answer = 1
            
while q :
    y = q.popleft(); x = q.popleft()
    for i in range(len(dx)) :
        new_y = y + dy[i]
        new_x = x + dx[i]
        
        if (new_x < 0 or new_x >= m or new_y < 0 or new_y >= n) :
            continue
        
        if tomato[new_y][new_x] == 0 :
            answer = tomato[y][x] + 1
            tomato[new_y][new_x] = answer
            q.append(new_y); q.append(new_x)

for y in range(n) :
    for x in range(m) :
        if tomato[y][x] == 0 :
            print(-1)
            exit()

print(answer - 1)