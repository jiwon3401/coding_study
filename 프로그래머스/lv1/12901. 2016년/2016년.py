def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU'] #1일 금요일
    days = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31] #윤년!!!
    #5월이면 4월까지 일수 더하고 +b 까지 더해준 뒤, 7로 나눔
    
    week_index = (sum(days[:a-1])+b)%7
    answer = week[week_index-1]
    return answer