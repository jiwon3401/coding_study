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

###############################################
#다른사람풀이 -> return값에 바로 (전체인원-짝지은수)=보트수 
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer