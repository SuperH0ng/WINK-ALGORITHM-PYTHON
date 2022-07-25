a, b = map(int, input().split())
count = 1

while a != b :
    count += 1
    if b % 10 == 1 :
        b = b // 10
    elif b % 2 == 1 or a > b:
        count = -1
        break
    else :
        b = b // 2

print(count)