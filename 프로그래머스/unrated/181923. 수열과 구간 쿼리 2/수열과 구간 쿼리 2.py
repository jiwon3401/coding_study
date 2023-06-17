def solution(arr,queries):
    answer=[]
    for query in queries:
        tmp=[]
        s,e,k=query
        for i in range(s,e+1):
            if arr[i]>k:
                tmp.append(arr[i])
        if len(tmp)==0:
            answer.append(-1)
        else:    
            answer.append(min(tmp))       
    return answer