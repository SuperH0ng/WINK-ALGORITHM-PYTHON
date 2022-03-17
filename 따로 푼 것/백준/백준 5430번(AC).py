import sys
input = sys.stdin.readline

def AC(order, imp, arr) :
    rev = 0
    st  = 0
    en = len(order)
    for i in range(len(order)) :
        if order[i] == 'R' :
            rev = 1 - rev
        else :
            if not rev :
                rev += 1
            else :
                en -= 1
        
        if st > en :
            return print("error")
    
    if not rev :
        return print(arr[st:en])
    else :
        return print(arr[st:en][::-1])

T = int(input())
for i in range(T) :
    o = input()
    l = input()
    a = input()
    a = list(map(int, a[1:-2].split(',')))
    AC(o, l, a)
