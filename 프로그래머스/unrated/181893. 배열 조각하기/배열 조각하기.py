def solution(arr, query):
    answer=arr.copy()
    for i in range(len(query)):
        if i%2==0:
            tmp = answer[:query[i]+1]
        else:
            tmp = answer[query[i]:]
        answer = tmp

    return answer