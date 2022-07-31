import sys
sys.setrecursionlimit(1000000007)

def mulMtx(a, b) :
    tmp = [[0, 0], [0, 0]]
    tmp[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000
    tmp[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000
    tmp[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000
    tmp[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000
    return tmp

def fibo(f) :
    if f == 1 :
        return [[1, 1], [1, 0]]
    
    mtx = fibo(f//2)
    if f % 2 == 0 :
        return mulMtx(mtx, mtx)
    else :
        return mulMtx(mulMtx(mtx, mtx), fibo(1))

n = int(input())
print(fibo(n-1)[0][0]) if n > 1 else print(1)