def solution(n):
    a = [0]*(n+1)
    for i in range(0,2):
        a[i]=1
    for i in range(2,n+1):
        a[i] = a[i-1]+a[i-2]
    
    return a[-1]%1234567