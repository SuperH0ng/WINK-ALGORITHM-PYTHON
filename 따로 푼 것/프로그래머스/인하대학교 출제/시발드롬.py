def solution1(palindrome):
    pList = list(palindrome)
    char = sorted(list(set(pList)))
    # minAlpha = pList[0]
    # for i in range(1, len(pList)) :
    #     if minAlpha > pList[i] :
    #         minAlpha = pList[i]
    
    if len(char) == 1 :
        return "IMPOSSIBLE"
    
    j = 0
    while (pList[j] == char[0]) :
        j += 1
    
    for l in range(len(palindrome)-1, len(palindrome) // 2 - 1, -1) :
        if pList[l] == char[0] :
            pList[j], pList[l] = pList[l], pList[j]
        
    return ''.join(pList)


# print(solution("aba"))

def solution2(palindrome):
    i = 1
    j = 1
    n = len(palindrome)
    while i < n :
        if palindrome[i] != palindrome[0]:
            break
        i += 1
    
    if i == n:
        return "IMPOSSIBLE"
    
    idx = n-1
    for j in range(n-2, 0, -1):
        if palindrome[j] < palindrome[idx]:
            idx = j
            # print(j)
    
    if palindrome[0] == palindrome[idx]:
        # print(idx, i)
        palindrome = list(palindrome)
        palindrome[idx] = palindrome[i]
        palindrome[i] = palindrome[0]
        palindrome = ''.join(palindrome)
        return palindrome
    
    # print(idx, i)
    palindrome = list(palindrome)
    palindrome[0] = palindrome[idx]
    palindrome[idx] = palindrome[n-1]
    palindrome = ''.join(palindrome)
    return palindrome


# print(solution("ccbbcc"))


import sys
import random
# input = sys.stdin.readline
    
while (True) :
    x = []
    rng = random.randrange(1, 100)
    for i in range(rng):
        x.append(chr(random.randrange(ord('a'),ord('z'))))
    x = ''.join(x)
    # print(x)
    x += x[len(x)-2::-1]
    # x += x[::-1]
    
    if solution1(x) != solution2(x) :
        print(x)
        print("찾았다!")
        break