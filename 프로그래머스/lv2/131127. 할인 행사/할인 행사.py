def solution(want, number, discount):
    '''
    discount : 날짜 순서대로 할인 정보를 나타냄
    '''
    from collections import Counter
    buy = dict(zip(want, number))
    
    # buy = {}
    # for w, n in zip(want, number):
    #     buy[w] = n
    
    cnt = 0
    for i in range(len(discount)-9):
        if Counter(discount[i:i+10])==buy:
            cnt +=1
    return cnt