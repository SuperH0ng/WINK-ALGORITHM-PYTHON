def solution(coin, k):
    coin += [2]
    coin0 = [0] * len(coin)
    coin1 = [1] * len(coin)
    answer = len(coin)
    
    count = 0
    for i in range(0,len(coin) - (k-1)) :
        if coin[i] != coin0[i] :
            for j in range(k) :
                coin[i + j] = 1 - coin[i + j]
            count += 1
    if coin[:-1] == coin0[:-1] :
        answer = min(answer, count)
        
    count = 0
    for i in range(0,len(coin) - (k-1)) :
        if coin[i] != coin1[i] :
            for j in range(k) :
                coin[i + j] = 1 - coin[i + j]
            count += 1
    if coin[:-1] == coin1[:-1] :
        answer = min(answer, count)
        
    
    return answer if answer < len(coin) else -1

