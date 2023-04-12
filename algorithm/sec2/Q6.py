#[#6. 자릿수의 합]
'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요. 
'''
import sys
input = sys.stdin.readline 
N = int(input())
nums = list(map(int, input().split()))

def digit_sum(x):
    num_sum = 0
    for i in str(x):
        num_sum += int(i)
    return num_sum

max = -float("inf")
for i in nums:
    digit_f = digit_sum(i)
    if digit_f > max:
        max = digit_f
        max_num = i
print(max_num)
        

#sol
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x): 
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum
max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x
print(res)        