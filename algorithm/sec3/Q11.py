#[#Q11. 격자판 회문수]
'''
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 
세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
'''
import sys
input = sys.stdin.readline 
m = [list(map(int, input().split())) for _ in range(7)]

cnt=0
for i in range(7):
    for j in range(2,5):
        if m[i][j-1] == m[i][j+1] and m[i][j-2] == m[i][j+2]:
            cnt+=1
        if m[j-1][i] == m[j+1][i] and m[j-2][i] == m[j+2][i]:
            cnt+=1
print(cnt)