def comb(number,n): 
    #[-1, 1, -1, 1]
    answer=[]     
    if n==0:
        return [answer]
    for i in range(len(number)):
        tmp=number[i]
        for j in comb(number[i+1:], n-1): 
            #([-1],combination([1,-1,1],2))+...
            answer.append([tmp]+j)
    return answer

def solution(number):
    answer = 0
    for i in comb(number,3):
        if sum(i)==0:
            answer+=1
    return answer
