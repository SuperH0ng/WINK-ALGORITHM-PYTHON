# import sys
# input = sys.stdin.readline

# str1 = input().strip()
# str2 = input().strip()

# LCS = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

# for i in range(len(str2)):
#     for j in range(len(str1)):
#         if str2[i] == str1[j]:
#             LCS[i+1][j+1] = LCS[i][j] + 1
#         else:
#             LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])

# print(LCS[len(str2)][len(str1)])


def solution(gene1, gene2):
    LCS = [[0] * (len(gene1)+1) for _ in range(len(gene2)+1)]
    
    # count1 = 0; count2 = 0
    # repeat1 = True; repeat2 = True
    
    # for s in gene1 :
    #     for i in range(len(gene2)) :
    #         if s == gene2[i] :
    #             count1 = i
    #             repeat1 = False
    #             break
    #     if repeat1 == False :
    #         break
        
    # for s in gene2 :
    #     for i in range(len(gene1)) :
    #         if s == gene1[i] :
    #             count2 = i
    #             repeat2 = False
    #             break
    #     if repeat2 == False :
    #         break
    
    
    
    for i in range(len(gene2)):
        for j in range(len(gene1)):
            if gene2[i] == gene1[j]:
                LCS[i+1][j+1] = LCS[i][j] + 1
                
            else:
                LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])

    return max(len(gene1), len(gene2)) - LCS[len(gene2)][len(gene1)] + 

print(solution("ACA", "CCCCG”"))