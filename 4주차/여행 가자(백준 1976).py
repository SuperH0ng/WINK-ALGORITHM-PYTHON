import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

travel = list(map(int,sys.stdin.readline().split()))

route = []
for k in range(N-1):
    route.append([k+1])

x = 0

while x < N-1 :
    for i in range(x+1,N):
        if lst[x][i] == 1 :
            route[x].append(i+1)
    
    x += 1

y = 0

while y < N-2 :
    for l in range(y+1, N-1):
        if set(route[y]) & set(route[l]) != set():
            route[l] = list(set(route[y]) | set(route[l]))
    print(route)
    y += 1




for y in route:
    if len(set(y) & set(travel)) == len(set(travel)) :
        result = True
        break
    else :
        result = False


print('YES' if result == True else 'NO')   

