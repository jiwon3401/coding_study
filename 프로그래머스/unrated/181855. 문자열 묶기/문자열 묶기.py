def solution(strArr):
    len_array = [len(i) for i in strArr]
    return max([len_array.count(i) for i in set(len_array)])