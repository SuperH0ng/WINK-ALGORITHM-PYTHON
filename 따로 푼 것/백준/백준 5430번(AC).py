import sys
input = sys.stdin.readline

def AC(order, imp, arr) :
    rev = 0
    st  = 0
    en = len(arr)
    for i in range(len(order)) :
        if order[i] == 'R' :
            rev = 1 - rev
            # print("첫 번째 if", rev)
        else :
            if not rev :
                st += 1
            else :
                en -= 1
            # print("첫 번째 else", st, en)
        if st > en :
            return print("error")
    
    s = ""
    if not rev :
        return print(str(arr[st:en]).replace(" ", ""))
    else :
        return print(str(arr[st:en][::-1]).replace(" ", ""))

T = int(input())
for i in range(T) :
    o = input().rstrip()
    l = int(input())
    if l == 0 :
        if 'D' in o :
            print('error')
        else :
            print([])
        input()
        continue

    a = input().rstrip()
    a = list(map(int, a[1:-1].split(',')))
    AC(o, l, a)
