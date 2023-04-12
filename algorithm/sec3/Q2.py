#[#2. 숫자만 추출]
'''
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다. 
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
'''
import sys 
input = sys.stdin.readline 
strings = input().strip() 
# import re
# nums = int(re.sub(r'[^0-9]', '', strings))
nums = []
for i in strings:
    if i.isdigit():
        nums.append(i)
nums = int(''.join(nums))
cnt = 0
for i in range(1,nums+1):
    if nums%i == 0:
        cnt+=1
print(nums)
print(cnt)


#sol
s = input()
res=0
for x in s:
    if x.isdecimal(): #isdecimal - 0~9까지만
        res = res*10+int(x)
        print(res)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i == 0:
        cnt+=1
print(cnt)
        