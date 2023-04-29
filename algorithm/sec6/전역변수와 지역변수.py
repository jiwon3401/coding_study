'''
전역 변수와 지역변수 
-> 지역변수가 먼저.
'''

def DFS1():
    cnt=3 #DFS1의 지역변수
    print(cnt) 
    
def DFS2():
    #1)
    # if cnt==5: #지역변수인가? -> X -> 전역변수로 작동
    #     print(cnt)
    
    #2)
    # if cnt==5:
    #     cnt=cnt+1 #지역변수로 인식은 했는데 값 할당이 안되서 에러
    #     print(cnt)
    
    #3)
    global cnt 
    if cnt==5: #cnt를 전역변수로 작동
        cnt+=1
        print(cnt) #3,6,6

if __name__ == "__main__":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)


##########################################################

def DFS():
    #1)
    #a[0]=7 #새로운 리스트 생성이 아님 -> a 인덱스 값을 변경(참조)
    
    #2)
    #a=a+[4] #a가 없어서 에러나므로 global a 선언해줘야함
    
    #3)
    a = [7,8] #새로운 local list가 생성된 것.
    print(a)


if __name__=="__main__":
    a = [1,2,3]
    DFS() 
    print(a) #3) 전역 리스트 [1,2,3] 출력