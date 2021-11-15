import sys
input = sys.stdin.readline

class OutOfRangeError(Exception) :
    def __init__(self):
        super().__init__('...')

commands = []

while True:

    while True :
        command = input().strip()
        if command != "END" :
            commands.append(command)
        else :
            break
    
    N = int(input())

    for i in range (N):
        stack = [int(input().strip())]
        try :
            for cmd in commands :
                if cmd[:3] == "NUM" :
                    stack.append(int(cmd[4:]))
                elif cmd == "POP" :
                    del stack[-1]
                elif cmd == "INV" :
                    stack[-1] *= -1
                elif cmd == "DUP" :
                    stack.append(stack[-1])
                elif cmd == "SWP" :
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                elif cmd == "ADD" :
                    stack.append(stack.pop()+stack.pop())
                elif cmd == "SUB":
                    stack.append(-1*stack.pop()+stack.pop())
                elif cmd == "MUL" :
                    stack.append(stack.pop()*stack.pop())
                elif cmd == "DIV" :
                    divisor, dividend = stack.pop(), stack.pop()
                    if divisor * dividend >= 0 :
                        stack.append(abs(dividend)//abs(divisor))
                    else :
                        stack.append(-1*(abs(dividend)//abs(divisor)))
                    
                elif cmd == "MOD" :
                    divisor, dividend = stack.pop(), stack.pop()
                    if dividend >= 0 :
                        stack.append(abs(dividend)%abs(divisor))
                    else :
                        stack.append(-1*(abs(dividend)%abs(divisor)))
                        
                if len(stack) != 0 and abs(stack[-1]) > 10**9 :
                        raise OutOfRangeError
            if len(stack) != 1:
                raise OutOfRangeError

        except IndexError:
            print("ERROR")
        except ZeroDivisionError :
            print("ERROR")
        except OutOfRangeError :
            print("ERROR")

        else :
            print(stack[0])

    input()
    
    cmd = input().strip()
    if cmd =="QUIT" :
        break
    else :
        print("")
        commands = [cmd]
