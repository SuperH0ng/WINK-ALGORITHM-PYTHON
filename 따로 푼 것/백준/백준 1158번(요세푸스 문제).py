from collections import deque
n,m = map(int,input().split())
q = deque([i for i in range(1,n+1)])
ans = []

while q:
    for c in range(m-1) :
        q.append(q.popleft())
    ans.append(str(q.popleft()))
    
print('<'+', '.join(ans)+'>')