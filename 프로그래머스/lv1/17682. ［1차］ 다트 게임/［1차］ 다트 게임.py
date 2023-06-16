def solution(darResult):
    ans_list = []
    indexs= -1
    tmp=0
    darResult=darResult.replace('10','P')
    for i in darResult:   
        if i.isdigit():
            tmp+=int(i)
            #indexs+=1      
        elif i=='P': #10 예외처리!!!!!! ㅠㅠ
            tmp+=10
        #제곱처리
        elif i == 'S':
            tmp = tmp**1
            ans_list.append(tmp)
            indexs+=1
            tmp=0
        elif i=='D':
            tmp = tmp**2
            ans_list.append(tmp)
            indexs+=1
            tmp=0
        elif i=='T':
            tmp = tmp**3
            ans_list.append(tmp)
            indexs+=1
            tmp=0
            
        # *, #  처리
        elif i == '#': # # * -> -1 처리
            ans_list[indexs] = ans_list[indexs]* -1
            
        elif i=='*': 
            #첫번째기회에 나올때
            if indexs==0:
                #tmp= darResult[indexs]*2
                ans_list[indexs] = ans_list[indexs]*2
            else:
                ans_list[indexs] = ans_list[indexs]*2
                ans_list[indexs-1] = ans_list[indexs-1]*2
    
    return sum(ans_list)