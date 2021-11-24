import sys

input = sys.stdin.readline
N = int(input())
wordToNum = {}
sum = 0
wordList = [input().strip() for i in range(N)]

for word in wordList :
    wordLen = len(word)
    for i in range(wordLen) :
        if word[i] not in wordToNum :
            wordToNum[word[i]] = 10**(wordLen - i - 1)
        else :
            wordToNum[word[i]] += 10**(wordLen - i - 1)
NumList = sorted(list(wordToNum.values()), reverse=True)

num = 9
sum = 0
for cnt in NumList :
    sum += num*cnt
    num -= 1
print(sum)

# print(wordToNumList)

# numList = sorted([input().strip() for i in range(N)], key = lambda x : len(x), reverse=True)
# num = 9
# wordToNum = {}
# sum = 0




# while len(numList[0]) > 0 :
#     if numList[0][0] in wordToNum :
#         sum += wordToNum[numList[0][0]] * (10**(len(numList[0])-1))
#         numList[0] = numList[0][1:]
#     else :
#         wordToNum[numList[0][0]] = num
#         sum += num * (10**(len(numList[0])-1))
#         numList[0] = numList[0][1:]
#         num -= 1    
#     numList = sorted(numList, key = lambda x : len(x), reverse=True)
# print(sum)