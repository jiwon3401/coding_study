def solution(people, limit):
    from collections import deque
    people.sort()
    w = deque(people) 
    answer = 0 

    while w:
        if len(w)==1:
            answer += 1
            break
        
        if w[0]+w[-1]>limit:
            w.pop()
            answer +=1
        else:
            w.popleft()
            w.pop()
            answer += 1
    return answer