from collections import deque

def find(a, b) :
    if a >= b :
        return a - b
    
    q = deque([a])
    while q :
        x = q.popleft()
        if x == b :
            return lst[x]
        if x > 0 and lst[x-1] == 0:
            lst[x-1] = lst[x] + 1
            q.append(x-1)
        if x < 100000 and lst[x+1] == 0:
            lst[x+1] = lst[x] + 1
            q.append(x+1)
        if x <= 50000 and lst[x*2] == 0:
            lst[x*2] = lst[x] + 1
            q.append(x*2)

n, k = map(int, input().split())
lst = [0] * 100001
print(find(n, k))