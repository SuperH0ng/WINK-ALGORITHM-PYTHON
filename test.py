import sys
input = sys.stdin.readline

N = int(input())
words = sorted([input().strip() for i in range(N)], key = lambda x : len(x), reverse= True)

# words = 
