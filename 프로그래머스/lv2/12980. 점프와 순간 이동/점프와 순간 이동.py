def solution(n):
    ans = 0
    while n: 
        ans+=n%2 #짝수->순간이동가능
        n=n//2
    return ans