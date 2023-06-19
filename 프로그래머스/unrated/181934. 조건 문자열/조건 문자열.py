def solution(ineq, eq, n, m):
    if eq=="=": 
        if ineq=="<":
            result=1 if n<=m else 0
        else:
            result=1 if n>=m else 0

    else:
        if ineq==">": 
            result=1 if n>m else 0
        else:
            result=1 if n<m else 0

    return result
