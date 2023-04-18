def solution(s, n):
    import re
    import string
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    answer = ''
    #s = list(re.sub(r"\s","",s))
    for i in s:
        #if i in " ":
        #    answer += " "
        if i in lowercase:
            answer += lowercase[(lowercase.find(i)+n)%26] 
        elif i in uppercase:
            answer += uppercase[(uppercase.find(i)+n)%26]
        else:
            answer += " "
    
    return answer