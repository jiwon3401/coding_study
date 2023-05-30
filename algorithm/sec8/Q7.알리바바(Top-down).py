#알리바바와 40인의 도둑(Top-down)

import sys
input = sys.stdin.readline 

def DP(x,y):
    if dy[x][y]>0: #cut edge
        return dy[x][y]
    
    if x==0 and y==0:
        return matrix[0][0] #(0,0)값
    
    else:
        if x==0:
            dy[x][y]=DP(x,y-1) + matrix[x][y] 
        elif y==0:
            dy[x][y]=DP(x-1,y) + matrix[x][y]
        else:
            dy[x][y]=min(DP(x-1,y)+matrix[x][y], DP(x,y-1)+matrix[x][y])
            #메모이제이션을 해줘야 time limit이 안남
        return dy[x][y]
        
if __name__=="__main__":
    N = int(input())
    matrix=[list(map(int, input().split())) for _ in range(N)]
    dy=[[0]*N for _ in range(N)] #dy[i][j]: 최소비용
    print(DP(N-1,N-1))