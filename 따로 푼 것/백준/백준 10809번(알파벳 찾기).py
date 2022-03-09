word = input()
count = [-1] * 26

for i in range(len(word)) :
    alpha = ord(word[i]) - ord('a')
    if count[alpha] == -1 :
        count[alpha] = i

for c in count :
    print(c, end=' ')