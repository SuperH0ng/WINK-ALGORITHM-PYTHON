import sys
input = sys.stdin.readline

n = int(input())
node = [[] for i in range(26)]

for i in range(n) :
    p, c1, c2 = input().split()
    
    node[ord(p) - ord('A')].extend([c1, c2])

def preorder_traverse(word) :
    if word == '.' :
        return
    idx = ord(word) - ord('A')
    print(word, end="")
    preorder_traverse(node[idx][0])
    preorder_traverse(node[idx][1])

def inorder_traverse(word) :
    if word == '.' :
        return
    idx = ord(word) - ord('A')
    inorder_traverse(node[idx][0])
    print(word, end="")
    inorder_traverse(node[idx][1])

def postorde_traverse(word) :
    if word == '.' :
        return
    idx = ord(word) - ord('A')
    postorde_traverse(node[idx][0])
    postorde_traverse(node[idx][1])
    print(word, end="")

preorder_traverse('A')
print()
inorder_traverse('A')
print()
postorde_traverse('A')
