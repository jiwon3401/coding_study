#최대 부분 증가수열(LIS: Longest Increasing Subsequence)
'''
N개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게 증가하는(작은 수에서 큰 수로) 원소들의 집합을 찾는 
프로그램을 작성하라. 예를 들어, 원소가 2, 7, 5, 8, 6, 4, 7,12, 3 이면 가장 길게 증가하도록 원소들을 
차례대로 뽑아내면 2, 5, 6, 7, 12를 뽑아내어 길이가 5인 최대 부분 증가수열을 만들 수 있다.
'''
import sys 
input=sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dy = [1]*N
for i in range(2,N):
    for j in range(i): 
        if seq[i]>seq[j]: #앞의 원소가 작은지 확인하고
            dy[i]=max(dy[i],dy[j]+1) #가장 max값을 찾아서 더해주면 됨
        
print(max(dy))
