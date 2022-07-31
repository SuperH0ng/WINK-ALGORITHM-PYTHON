# 각 사람마다 dictionary로 넘버링을 해줄건데
# dictionary에 사람이 없다면 추가해주고 num을 1씩 더함
# 각 사람의 num을 통해 유니온 파인드하면 될 듯?
# 크기.. .. .. 

import sys
input = sys.stdin.readline

t = int(input())

def findRoot(arr, cur) :
    if arr[cur][0] == cur :
        return cur
    arr[cur][0] = findRoot(arr, arr[cur][0])
    return arr[cur][0]

for i in range(t) :
    n = int(input())
    num = 1
    
    social = [[i,1] for i in range(200001)]
    check = {}
    
    for j in range(n) :
        a, b = input().split()
        
        if not check.get(a) :
            check[a] = num
            num += 1
        if not check.get(b) :
            check[b] = num
            num += 1
        # print("num :", num)
        aNum = check.get(a)
        bNum = check.get(b)
        aNum, bNum = min(aNum, bNum), max(aNum, bNum)
        roota = findRoot(social, aNum)
        rootb = findRoot(social, bNum)
        # print(a, "와", b, "의 root :", roota, rootb)
        if not (rootb == roota) :
            # print("다르면 출력")
            social[rootb][0] = social[roota][0]
            social[roota][1] += social[rootb][1]
        
        # print("social :", social[:5])
        print(social[roota][1])
        
    social.clear()
