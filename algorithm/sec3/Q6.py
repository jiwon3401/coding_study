#[#Q6. 격자판 최대합]
'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.
'''
import sys
input = sys.stdin.readline 
N = int(input())
matrix = []
matrix_sum = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

diag_sum,diag_sum2= 0,0
for i in range(N):
    diag_sum += matrix[i][i]
    diag_sum2 += matrix[i][N-i-1]
    col_sum, row_sum = 0,0
    for j in range(N):
        col_sum += matrix[j][i]
        row_sum += matrix[i][j]
    matrix_sum.append(row_sum)
    matrix_sum.append(col_sum)
matrix_sum.append(diag_sum) 
matrix_sum.append(diag_sum2) 
print(max(matrix_sum))


#sol
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][j]
    if sum1>largest:
        largest = sum1
    if sum2>largest:
        largest = sum2

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][N-1-i]
if sum1>largest:
    largest = sum1
if sum2>largest:
    largest = sum2
print(largest)