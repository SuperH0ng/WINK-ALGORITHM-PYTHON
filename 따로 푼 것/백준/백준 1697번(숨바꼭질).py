# from collections import deque

# def find(a, b) :
#     if a >= b :
#         return a - b
    
#     q = deque([a])
#     while q :
#         x = q.popleft()
#         if x == b :
#             return lst[x]
#         if x > 0 and lst[x-1] == 0:
#             lst[x-1] = lst[x] + 1
#             q.append(x-1)
#         if x < 100000 and lst[x+1] == 0:
#             lst[x+1] = lst[x] + 1
#             q.append(x+1)
#         if x <= 50000 and lst[x*2] == 0:
#             lst[x*2] = lst[x] + 1
#             q.append(x*2)

# n, k = map(int, input().split())
# lst = [0] * 100001
# print(find(n, k))

from collections import deque
import sys
input = sys.stdin.readline
MAX_VALUE = 100000

n, k = map(int, input().split())

if n >= k :
    print(n - k)
    exit()

graph = [0] * (MAX_VALUE + 1)
q = deque([n])

while q :
    pos = q.popleft()
    if pos == k :
        print(graph[pos])
        exit()
    if pos > 0 and graph[pos-1] == 0 :
        graph[pos-1] = graph[pos] + 1
        q.append(pos - 1)
    if pos < MAX_VALUE and graph[pos+1] == 0 :
        graph[pos+1] = graph[pos] + 1
        q.append(pos + 1)
    if pos <= (MAX_VALUE//2) and graph[pos*2] == 0 :
        graph[pos*2] = graph[pos] + 1
        q.append(pos*2)