n = int(input())
s = input()

sum = 0
for i in range(n) :
    mul = (ord(s[i]) - ord('a') + 1)
    
    cnt = i
    while cnt > 0 :
        mul = (mul * 31) % 1234567891
        cnt -= 1
    
    sum += mul
    sum %= 1234567891

print(sum)
