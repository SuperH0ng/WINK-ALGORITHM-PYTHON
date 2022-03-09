n = int(input())
for num in range(n + 1) :
    answer = sum(map(int, str(num))) + num
    if answer == n :
        print(num)
        break
    if num == n :
        print(0)