N = int(input())

passBy = 1
door = (N-2) // 6

while door >= 0:
    door -= passBy
    passBy += 1

print(passBy)
