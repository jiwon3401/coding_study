'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
    
N = int(input())
num_array = []
for _ in range(N):
    num = int(input())
    num_array.append(num)
    

for i in range(N-1):
    for j in range(N-i-1):
        if num_array[j] > num_array[j+1]:
            num_array[j], num_array[j+1] = num_array[j+1], num_array[j]
            
for i in num_array:
    print(i)
