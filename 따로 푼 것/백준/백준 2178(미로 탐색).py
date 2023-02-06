from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = list(input().strip() for i in range(n))

graph = list([1] * m for i in range(n))

q = deque([0, 0])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q :
    y = q.popleft()
    x = q.popleft()
    
    for i in range(len(dx)) :
        new_y = y + dy[i]
        new_x = x + dx[i]
        
        if (new_x < 0 or new_x >= m or new_y < 0 or new_y >= n) :
            continue
        
        if graph[new_y][new_x] == 1 and maze[new_y][new_x] == '1' :
            graph[new_y][new_x] = graph[y][x] + 1
            q.append(new_y)
            q.append(new_x)

print(graph[-1][-1])
    
