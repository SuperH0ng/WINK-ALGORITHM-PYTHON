from collections import deque
import sys
input = sys.stdin.readline

maxint = sys.maxsize
q = deque()

n = int(input())
m = int(input())

bus = [{} for i in  range(1001)]
cost = [maxint] * 1001

for i in range(m) :
    s, e, c = map(int, input().split())
    if e in bus[s] :
        bus[s][e] = min(bus[s][e], c)
    else :
        bus[s][e] = c

depart, arriv = map(int, input().split())
cost[depart] = 0
q.append([depart, 0])

while q :
    e, c = q.popleft()
    
    if cost[e] < c :
        continue
    
    for key in bus[e] :
        if cost[e] == maxint :
            continue
        newc = bus[e][key] + c
        if newc < cost[key]:
            cost[key] = newc
            q.append([key, newc])
    
print(cost[arriv])
