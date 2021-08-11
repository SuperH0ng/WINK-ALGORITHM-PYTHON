def solution(price, money, count):


    price = ((count*(count+1))//2) * price

    if (price-money) > 0 :
        result = price-money
    else :
        result = 0
    

    return result
