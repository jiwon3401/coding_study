def solution(citations):
    answer=0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]<(i+1): ###
            return i
        
    return len(citations) #[5,5,5,5]일 경우