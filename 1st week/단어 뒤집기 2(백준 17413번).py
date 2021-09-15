import sys
S = sys.stdin.readline().strip()

string = ''
tag = False

for _ in S :
    if tag == True and _ != '>':
        string += _
    elif _ == '<':
        string = string[::-1]
        print(string, end='')
        string = ''
        tag = True
        string += _
    elif _ == '>':
        string += _
        tag = False
        print(string, end='')
        string = ''
    elif tag == False and _ != ' ':
        string += _
    else :
        string = string[::-1]
        print(string, end=' ')
        string = ''
print(string[::-1])
