import sys
N, M = map(int, sys.stdin.readline().split())

A = [list(sys.stdin.readline().strip()) for _ in range(N)]
B = [list(sys.stdin.readline().strip()) for _ in range(N)]

count = 0

def change(x,y) :
    if A[x][y] != B[x][y] :
        for i in range(x,x+3) :
            for l in range(y,y+3) :
                A[i][l] = str((int(A[i][l])+1)%2)
        global count
        count += 1

over = True
for j in range(0,N-2) :
    for k in range(0,M-2) :
        change(j,k)

        if A == B :
            over = False
            break
    if over == False :
        break

print(count if A == B else -1)