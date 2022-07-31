from collections import deque

n = int(input())
q = deque()

for i in range(n,0,-1) :
    q.append(i)

while len(q) > 1 :
    q.pop()
    q.appendleft(q.pop())

print(q.pop())
