import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

LCS = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            LCS[i+1][j+1] = LCS[i][j]
        else:
            LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])

print(LCS[len(str1)][len(str2)])
