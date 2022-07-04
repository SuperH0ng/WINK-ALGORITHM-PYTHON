import sys
input = sys.stdin.readline

n = int(input())

for i in range(n) :
    s = input()
    
    password = []
    stack = []
    for l in range(len(s)) :
        k = s[l] 
        if k == "<" :
            if password :
                stack.append(password.pop())
        elif k == ">" :
            if stack :
                password.append(stack.pop())
        elif k == "-" :
            if password :
                password.pop()
        else :
            password.append(k)
            
        # print("sub :",password)

    print("".join(password[:-1]) + "".join(stack[::-1]))
