import numpy as np
from collections import Counter

def solution(k, tangerine):
    answer = 0
    #counts = list(Counter(tangerine).values())
    #counts.sort(reverse=True)
    counts= np.sort(np.unique(np.array(tangerine), return_counts=True)[1])[::-1]
    tmp=0
    for i in counts:
        answer +=1
        tmp+= i
        if tmp>=k:
            break
    
    return answer