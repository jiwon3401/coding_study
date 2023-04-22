from itertools import combinations
def solution(numbers):
    answer = []
    comb = list(combinations(numbers,2))
    for i in comb:
        answer.append(i[0]+i[1])
    answer.sort()
    
    ans =[]
    for i in answer:
        if i not in ans:
            ans.append(i)
    return ans