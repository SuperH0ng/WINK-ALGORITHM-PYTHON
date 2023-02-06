from collections import deque
import sys
INF = sys.maxsize
start, end = map(int, input().split())

def find(s, e) :
    loc = [INF] * 100001
    visited = [False] * 100001
    loc[s] = 0
    visited[s] = True
    q = deque()
    q.append(s)

    while q :
        n = q.popleft()
        if n < 0 or n > 100000 :
            continue
        
        if n <= 50000 and not visited[2*n]:
            loc[2*n] = min(loc[2*n], loc[n])
            visited[2*n] = True
            q.appendleft(2*n)
        if n < 100000 and not visited[n+1]:
            loc[n+1] = min(loc[n+1], loc[n]+1)
            visited[n+1] = True
            q.append(n+1)
        if n > 0 and not visited[n-1]:
            loc[n-1] = min(loc[n-1], loc[n]+1)
            visited[n-1] = True
            q.append(n-1)
            
        if n == e :
            break
    
    print(loc[e])

find(start, end)