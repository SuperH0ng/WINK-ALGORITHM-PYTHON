import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
lst = []
check = [[0]*n for i in range(n)]
checkRG =[[0]*n for i in range(n)]
answer = 0
answerRG = 0
for i in range(n) :
    arr = []
    s = input()
    for j in range(n) :
        if s[j] == 'B' :
            arr.append(0)
        elif s[j] == 'R' :
            arr.append(1)
        else :
            arr.append(2)
    lst.append(arr)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque([])
queueRG = deque([])

for i in range(n) :
    for j in range(n) :
        if check[i][j] == 0 :
            answer += 1
            check[i][j] = answer
            queue.append([i, j])

            while queue :
                x, y = queue.popleft()
                # check[x][y] = answer
                for l in range(4) :
                    r = x + dx[l]
                    c = y + dy[l]
                    if r < 0 or r >= n or c < 0 or c >= n :
                        continue
                    if lst[x][y] == lst[r][c] and check[r][c] == 0:
                        check[r][c] = answer
                        queue.append([r,c])

        if checkRG[i][j] == 0 :
            answerRG += 1
            checkRG[i][j] = answerRG
            queueRG.append([i, j])

            while queueRG :
                x, y = queueRG.popleft()
                # checkRG[x][y] = answerRG
                for l in range(4) :
                    r = x + dx[l]
                    c = y + dy[l]
                    if r < 0 or r >= n or c < 0 or c >= n :
                        continue
                    if checkRG[r][c] == 0:
                        if ((lst[x][y] and lst[r][c]) or (not lst[x][y] and not lst[r][c])) :
                            checkRG[r][c] = answerRG
                            queueRG.append([r,c])

print(answer, answerRG)