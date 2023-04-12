#재귀함수와 스택
import sys 
input = sys.stdin.readline 
#재귀함수 -> 반복문의 대체

def DFS(x):
    if x>0:     
        #print(x) # 3 2 1 
        DFS(x-1)
        print(x, end=' ') # 1 2 3
    
    
if __name__ == "__main__":
    n = int(input())
    DFS(n)

