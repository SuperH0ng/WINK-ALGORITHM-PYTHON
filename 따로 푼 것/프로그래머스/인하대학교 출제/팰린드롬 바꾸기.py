def solution(palindrome):
    pList = list(palindrome)
    char = sorted(list(set(pList)))
    if len(char) == 1 :
        return "IMPOSSIBLE"
    j = 0
    while (pList[j] != char[0]) :
        j += 1
    for l in range(len(palindrome)-1, len(palindrome) // 2 - 1, -1) :
        if pList[l] == char[0] :
            pList[j], pList[l] = pList[l], pList[j]
    return ''.join(pList)