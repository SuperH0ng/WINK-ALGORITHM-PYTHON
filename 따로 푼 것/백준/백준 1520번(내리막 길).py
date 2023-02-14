import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

m, n = map(int, input().split())

road = list(list(map(int, input().split())) for i in range(m))
check = list([False] * n for i in range(m))
cost = list([0] * n for i in range(m))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def downhill(y, x) :
    
    if y == 0 and x == 0 :
        return 1

    if check[y][x] == True :
        return cost[y][x]
    
    check[y][x] = True

    for i in range(len(dx)) :
        new_y = y + dy[i]
        new_x = x + dx[i]
        
        if (new_x < 0 or new_x >= n or new_y < 0 or new_y >= m) :
            continue

        if (road[new_y][new_x] > road[y][x]) :
            cost[y][x] += downhill(new_y, new_x)
    
    return cost[y][x]

print(downhill(m-1, n-1))