n = int(input())

lst = [0,1]

i = 2
while (i <= n) :
    lst.append(lst[-1] + lst[-2])
    i += 1

print(lst[-1])