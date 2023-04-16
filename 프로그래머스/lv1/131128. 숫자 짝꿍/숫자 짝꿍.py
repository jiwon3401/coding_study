def solution(X, Y):
    from collections import Counter 
    answer = ''
    common = sorted(list((Counter(X)&Counter(Y)).elements()), reverse=True)

    if common:
        if common[0]=='0':
            answer = '0'
        else:
            answer = str(''.join(common))
    else:
        answer = '-1'

    return answer