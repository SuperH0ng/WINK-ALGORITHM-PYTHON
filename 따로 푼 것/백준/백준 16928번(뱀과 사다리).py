import sys
input = sys.stdin.readline
from collections import deque

l, s = map(int, input().split())
ladder = dict([list(map(int, input().split())) for _ in range(l)])
snake = dict([list(map(int, input().split())) for _ in range(s)])
isVisit = [False] * 101
isVisit[1] = True
pathCount = [0] * 101

q = deque()
q.append(1)
while q : 
    tmp = q.popleft()
    
    if tmp in ladder and not isVisit[ladder[tmp]] :
        q.append(ladder[tmp])
        isVisit[ladder[tmp]] =True
        pathCount[ladder[tmp]] = pathCount[tmp]

    if tmp in snake and not isVisit[snake[tmp]] : 
        q.append(snake[tmp])
        isVisit[snake[tmp]] =True
        pathCount[snake[tmp]] = pathCount[tmp]

    for i in range(1, 7) :
        if tmp + i <= 100 and not isVisit[tmp+i]:
            q.append(tmp+i)
            isVisit[tmp+i] = True
            pathCount[tmp+i] = pathCount[tmp] + 1

print(pathCount[100])
