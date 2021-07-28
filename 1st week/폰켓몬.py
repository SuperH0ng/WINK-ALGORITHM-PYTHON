def solution(nums):
    lst = []
    for _ in nums :
        if _ not in lst:
            lst.append(_)
    answer = min(len(lst), (len(nums)/2))
    return answer
