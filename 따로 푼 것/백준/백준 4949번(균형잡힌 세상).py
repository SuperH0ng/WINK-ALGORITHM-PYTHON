import sys
input = sys.stdin.readline

while 1 :
    s = input().rstrip()
    if s == "." :
        break
    
    check = True
    stack = []
    for w in s :
        if w == "(" :
            stack.append(")")
        elif w == "[" :
            stack.append("]")
        elif w == ")" or w == "]":
            if not stack or w != stack.pop() :
                check = False
                break
    
    if check and not len(stack):
        print("yes")
    else :
        print("no")