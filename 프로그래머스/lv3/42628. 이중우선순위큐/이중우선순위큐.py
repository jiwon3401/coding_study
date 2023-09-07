def solution(operations):
    import re
    import heapq as hq
    aa = []
    for i in operations:
        if i.startswith("I"):
            _, nums = i.split()
            hq.heappush(aa, int(nums))
        elif i=='D -1':
            #최솟값 삭제
            if aa:
                hq.heappop(aa)

        elif i=='D 1':
            #최댓값 삭제
            if aa:
                aa.remove(max(aa))

    if len(aa)==0:
        return [0,0]
    return [max(aa), hq.heappop(aa)]