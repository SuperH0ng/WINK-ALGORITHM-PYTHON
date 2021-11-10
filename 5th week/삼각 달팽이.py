def toBottom(arr, x, y, num, cnt) :
    for i in range(cnt) : 
        x, num = x+1, num+1
        arr[x][y] = num
    cnt -= 1
    if cnt == 0 :
        return arr
    toRight(arr, x, y, num, cnt)
    
def toRight(arr, x, y, num, cnt) :
    for i in range(cnt) : 
        y, num = y+1, num+1
        arr[x][y] = num
    cnt -= 1
    if cnt == 0 :
        return arr
    toLeftTop(arr, x, y, num, cnt)
    
def toLeftTop(arr, x, y, num, cnt) :
    for i in range(cnt) : 
        x, y, num = x-1, y-1, num+1
        arr[x][y] = num
    cnt -= 1
    if cnt == 0 :
        return arr
    toLeftTop(arr, x, y, num, cnt)
    


def solution(n):
    answerList = [[0] * n for _ in range(n)]
    
    answerList[0][0] = 1
    toBottom(answerList, 0, 0, 1, n-1)
    
    answer = []
    
    for i in range(n) :
        for j in range(n) :
            if answerList[i][j] == 0 :
                break
            answer.append(answerList[i][j])
    
    return answer

n = int(input())
solution(n)