import sys
input = sys.stdin.readline

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            try:
                if j == 0:
                    raise IndexError
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            except IndexError:
                if j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
    return max(triangle[-1])


print(solution(triangle))
