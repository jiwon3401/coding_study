def solution(rank, attendance):
    from collections import OrderedDict
    
    test_dict = dict(zip(rank,attendance))
    test_dict = OrderedDict(sorted(test_dict.items(), key = lambda item: item[0]))
    answer=[]
    for k,v in test_dict.items():
        if len(answer)==3:
            break   
            
        if v==True:
            answer.append(rank.index(k))
        else:
            pass
    
        if len(answer)==3:
            break   
            
    return 10000*answer[0]+100*answer[1]+answer[2]