def solution(k,score):
    best=[] 
    worst=[]
    for i in range(len(score)):
        if i<=k-1:
            best.append(score[i])
            worst.append(min(best))
        else:
            best.sort()
            if score[i]>min(best):
                best.pop(0)
                best.append(score[i])
                worst.append(min(best))
            else:
                worst.append(min(best))
    return worst
