def solution(triangle):
    #dy = [[0 for j in i]for i in triangle]
    #dy[0][0]=triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(i+1): #인덱스
            #가장 오른쪽, 왼쪽은 위에 것 그대로 가져오기
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
                
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
                
    return max(triangle[-1])