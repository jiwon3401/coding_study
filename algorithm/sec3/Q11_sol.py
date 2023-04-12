import sys   
input = sys.stdin.readline 
board = [list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5] #행 탐색
        if tmp==tmp[::-1]: 
            cnt+=1
            
        for k in range(2): #열 탐색 -> 슬라이싱 사용못하므로.
            if board[i+k][j] != board[i+5-k-1][j]: 
                break
        else:
            cnt+=1
print(cnt) 