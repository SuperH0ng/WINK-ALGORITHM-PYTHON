import sys

N = sys.stdin.readline().strip()
l = len(N)

if l%2 == 0:
    pal = N[:(l//2)]+ N[(l//2)-1::-1]
    if int(N) < int(pal):
        print(int(pal))
    elif N[(l//2)-1] != '9':
        pal = pal[:(l//2)-1] + str(int(pal[(l//2)-1])+1)*2 + pal[(l//2)+1:]
        print(int(pal))
    else :
        pal = str(int(pal[:(l//2)])+1)
        pal = pal + pal[(l//2)-1::-1]
        print(int(pal))

elif l != 1 :
    pal = N[:(l//2)+1] + N[(l//2)-1::-1]
    if int(N) < int(pal):
        print(int(pal))
    elif N[(l//2)] != '9':
        pal = str(int(N[:(l//2)+1])+1) + N[(l//2)-1::-1]
        print(int(pal))
    else :
        pal = str(int(pal[:(l//2+1)])+1)
        pal = pal + pal[(l//2)-1::-1]
        print(int(pal))

elif N != '9' :
    print(int(N)+1)

else :
    print(11)
    