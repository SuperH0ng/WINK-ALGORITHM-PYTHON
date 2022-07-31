import sys
from queue import PriorityQueue
input = sys.stdin.readline
q = PriorityQueue()

n = int(input())

for i in range(n) :
    tmp = list(map(int, input().split()))
    
    if tmp[0] == 0 :
        if q.queue :
            print(-q.get())
        else :
            print(-1)
    
    else :
        for j in range(tmp[0]) :
            q.put(-tmp[j+1])
