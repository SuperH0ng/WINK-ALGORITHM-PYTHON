import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for c in range(t) : 
    start, end = map(int, input().split())
    isVisit = [False] * 10000
    isVisit[start] = True
    path = [""] * 10000
    q = deque()
    q.append(start)

    while q : 
        tmp = q.popleft()

        # D *2
        op = (tmp*2) % 10000
        if not isVisit[op] :
            q.append(op)
            path[op] = path[tmp] + 'D'
            isVisit[op] = True

        # S -1
        op = (tmp-1) % 10000
        if not isVisit[op] :
            q.append(op)
            path[op] += path[tmp] + 'S'
            isVisit[op] = True

        # L <1
        op = (tmp % 1000) * 10 + tmp // 1000

        if not isVisit[op] :
            q.append(op)
            path[op] += path[tmp] + 'L'
            isVisit[op] = True
        
        # R >1
        op = (tmp % 10) * 1000 + tmp // 10

        if not isVisit[op] :
            q.append(op)
            path[op] += path[tmp] + 'R'
            isVisit[op] = True

    print(path[end])