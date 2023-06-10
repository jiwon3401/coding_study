def solution(board, moves):
    stack = []
    answer=0
    for i in moves:
        for j in range(len(board)):
            #board 열 -> 0이 아닌 부분이 stack에 들어감
            if board[j][i-1]==0:
                continue
                
            elif board[j][i-1]!=0:
                # if len(stack)==0:
                #     stack.append(board[j][i-1])
                #     break
                # else:
                stack.append(board[j][i-1])
                board[j][i-1]=0 #append했으면 원소 0으로 바꿔줘야함

                if len(stack)>1:   #2개 이상은 쌓여야하므로
                    if stack[-1]==stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer+=2   
            break
            
    return answer