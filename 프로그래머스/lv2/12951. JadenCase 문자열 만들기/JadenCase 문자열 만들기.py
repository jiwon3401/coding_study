def solution(s):
    answer = []
    ss = s.split(' ')
    for i in ss:
        if i:
            answer.append(i[0].upper()+i[1:].lower())
        else:
            answer.append(i)
    return " ".join(answer)