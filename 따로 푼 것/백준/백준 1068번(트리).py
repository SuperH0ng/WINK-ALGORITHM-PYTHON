N = int(input())
tree = list(map(int, input().split()))
d = int(input())

def findParent(node) :
    if node == d :
        return d
    elif node == -1 :
        return -1
    else :
        return findParent(tree[node])

for i in range(N) :
    p = findParent(i)
    if p == d :
        tree[i] = d

# print("tree :", tree)
check = [1] * N

for i in range(N) :
    if tree[i] == d :
        check[i] = 0
    elif tree[i] == -1 :
        continue
    else :
        check[tree[i]] = 0

# print("check :",check)
print(sum(check))