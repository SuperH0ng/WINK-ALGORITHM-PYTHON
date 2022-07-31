import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n+1)]

def findRoot(cur) :
    if arr[cur] == cur :
        return cur
    arr[cur] = findRoot(arr[cur])
    return arr[cur]

count = 0
check = False
while m > 0 :
    count += 1
    m -= 1
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    roota = findRoot(a); rootb = findRoot(b)
    if roota == rootb :
        check = True
        break
    else :
        arr[rootb] = arr[roota]

if check :
    print(count)
else :
    print(0)