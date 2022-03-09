import sys
input = sys.stdin.readline

n = int(input())
words = list(set([input().strip() for i in range(n)]))
words.sort(key = lambda x : (len(x), x))

for w in words :
    print(w)