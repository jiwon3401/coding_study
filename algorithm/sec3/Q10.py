#[#Q10. 스도쿠 검사]
'''
스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출력하는 프로그램을 작성하세요.
'''
import sys
input = sys.stdin.readline
a = [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        check1 = [0]*10
        check2 = [0]*10
        for j in range(9):
            check1[a[i][j]] = 1 #행 체크
            check2[a[j][i]] = 1 #열 체크
        if sum(check1)!=9 or sum(check2)!=9:
            return False
        
    #그룹 탐색
    for i in range(3):
        for j in range(3): #그룹 정하기
            check3 = [0]*10
            for k in range(3): #그룹 정해지면 그 안에 있는 숫자 확인
                for s in range(3):
                    check3[a[i*3+k][j*3+k]] = 1
            if sum(check3) != 9:
                return False
    return True 

if check(a):
    print("Yes")
else: print("No")