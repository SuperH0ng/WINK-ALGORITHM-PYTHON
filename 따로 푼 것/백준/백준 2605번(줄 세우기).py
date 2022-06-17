n = int(input())
order = [1]
num = [0] + list(map(int, input().split()))
for i in range(2,n+1) :
    order.insert(num[i], i)

for i in range(n-1, -1, -1) :
    print(order[i], end=" ")