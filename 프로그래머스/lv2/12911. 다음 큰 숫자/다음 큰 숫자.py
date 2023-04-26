def solution(n):
    answer=0
    count_one = bin(n)[2:].count('1') #input 1의 개수
    for i in range(n+1, 1000001):
        if bin(i)[2:].count('1') == count_one:
            answer = i
            break
    return answer