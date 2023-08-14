def solution(clothes):
    #하루에 최소 한개의 의상은 입음!
    p = dict()
    answer=1
    for i in clothes:
        p[i[1]] = p.get(i[1],0)+1    

    for k,v in p.items():
        #(a+1)(b+1)-1
        answer*=(v+1) #해당 아이템 안 입는경우
    
    return answer-1 #전체 안입는 경우는 제외


#틀린 풀이
# def solution(clothes):
#     answer = 0
#     tmp=1
#     p = dict()
#     for i in clothes:
#         p[i[1]]=p.get(i[1],0)+1
    
#     for idx, (k,v) in enumerate(p.items()):
#         answer+=v 
#         tmp*=v 
#         if len(p)==1:
#             break
#         elif tmp!=1 and idx == len(p)-1:
#             answer+=tmp  
#     return answer