import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0 for i in range(n)] for j in range(m)] 

for i in range(k) :
    lx, ly, rx, ry = map(int, input().split())

    for j in range(ly, ry) :
        for l in range(lx, rx) :
            arr[j][l] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
anscnt = 0
answer = []
q = deque()
checkList = arr[:]
for i in range(m) :
    for j in range(n) :

        if not checkList[i][j] :
            checkList[i][j] = 1
            q.append([i, j])

            area = 0
            while q :
                y, x = q.popleft()
                area += 1

                for d in range(4) :
                    yy = y + dy[d]
                    xx = x + dx[d]

                    if yy >= m or yy < 0 or xx >= n or xx < 0 :
                        
                        continue
                    if checkList[yy][xx] :
                        continue

                    q.append([yy,xx])
                    checkList[yy][xx] = 1
                # print("여기가 문젠가?")
                

            anscnt += 1
            answer.append(area)

answer.sort()
print(anscnt)
for i in range(anscnt) :
    print(answer[i], end=" ")