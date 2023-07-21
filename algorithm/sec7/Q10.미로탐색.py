#[Q10.미로탐색(DFS)]
import sys
input = sys.stdin.readline

#back할때 check 풀어서 다시 방문할 수 있게 해야함
#bfs랑 다른점 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x,y):
    global answer
    if x==6 and y==6:
        answer+=1
    else:
        for i in range(4): #상하좌우
            x_pos = x+dx[i]
            y_pos = y+dy[i]
            if 0<=x_pos<=6 and 0<=y_pos<=6 and board[x_pos][y_pos]==0:
                board[x_pos][y_pos]=1
                DFS(x_pos, y_pos)
                board[x_pos][y_pos]=0 #back해서 되돌아갈 때 check풀어서 다시 방문할 수 있게 해야함 !
    
    
if __name__=="__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    board[0][0]=1 #방문했으니 check
    answer=0
    DFS(0,0)
    print(answer)
    