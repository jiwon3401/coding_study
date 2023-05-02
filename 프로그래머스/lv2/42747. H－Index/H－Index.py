def solution(citations):
    citations.sort(reverse=True)
    answer=0
    for i in range(len(citations)):
        if citations[i]>=i: #h번 이상 인용이 h개
            answer+=1
    return answer