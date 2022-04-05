def mulMtx(a, b, n) :
    result = [[0] * n for i in range(n)]
    for i in range(n) :
        for j in range(n) :
            sum = 0
            for l in range(n) :
                sum = (sum + a[i][l] * b[l][j]) % 1000
            result[i][j] = sum
    return result

def power(size, p) :
    if p == 1 :
        return matrix
    mtx = power(size, p//2)
    if p % 2 == 0 :
        return mulMtx(mtx, mtx, size)
    else :
        return mulMtx(mulMtx(mtx, mtx, size), power(size, 1), size)


import sys
ipt = sys.stdin.readline
n, b = map(int, ipt().split())
matrix = [list(map(lambda x : int(x) % 1000, ipt().split())) for i in range(n)]

answer = power(n, b)
for i in range(n) :
    for j in range(n) :
        print(answer[i][j], end = " ")
    print()