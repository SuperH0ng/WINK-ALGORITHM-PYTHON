def solution(coin, k):
    coin += [2] * (k-1)
    copyCoin = coin[:]
    coin0 = [0] * len(coin)
    coin1 = [1] * len(coin)
    answer = len(coin)
    
    count = 0
    for i in range(0,len(coin) - (k-1)) :
        if coin[i] != coin0[i] :
            for j in range(k) :
                coin[i + j] = 1 - coin[i + j]
            count += 1
    if coin[:-k] == coin0[:-k] :
        answer = count
    
    count = 0
    coin = copyCoin
    for i in range(0,len(coin) - (k-1)) :
        if coin[i] != coin1[i] :
            for j in range(k) :
                coin[i + j] = 1 - coin[i + j]
            count += 1
    if coin[:-k] == coin1[:-k] :
        answer = min(answer, count)
        
    
    return answer if answer < len(coin) else -1