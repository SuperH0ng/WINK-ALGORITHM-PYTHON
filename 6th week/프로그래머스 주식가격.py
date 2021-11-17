def solution(prices):
    time = 1
    answer = []
    for i in range(len(prices)-1) :
        for j in range(i+1, len(prices) - 1):
            if prices[i] <= prices[j] :
                time += 1
            else : 
                break
        
        answer.append(time)
        time = 1
        
    answer.append(0)
    return answer