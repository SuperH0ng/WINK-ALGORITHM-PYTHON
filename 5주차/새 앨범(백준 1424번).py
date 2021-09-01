import sys

from math import ceil

N = int(sys.stdin.readline().strip())
L = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

x = 0
while x <= (C+1)/(L+1) - 1 :
    x += 1

if x%13 == 0 :
    x -= 1   

if N%x != 13 :
    print(ceil(N/x))
elif x - N%x != 1 :
    print(ceil(N/x))
else :
    print(ceil(N/x)+1)