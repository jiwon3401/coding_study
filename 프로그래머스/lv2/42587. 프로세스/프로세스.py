def solution(priorities, location):
    from collections import deque
    answer = 0
    priorities=deque(priorities)
    index = deque(range(0,len(priorities)))
    while priorities:
        max_p = max(priorities)
        if priorities[0]==max_p: #첫번째 순서에 있을때
            answer += 1
            if index[0]==location: #location 반환 
                break
            else: #순서나올때까지
                priorities.popleft()
                index.popleft()
        else:
            priorities.append(priorities.popleft())
            index.append(index.popleft())
    return answer