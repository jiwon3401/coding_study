#[#Q3. 후위표기식 만들기]
#꼭 다시 풀어보기
'''
중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰는 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면 (3+5)*2 이면 35+2* 로 바꾸어야 합니다.
'''

aa = list(input())
stack = []
res = '' #숫자만 뽑아내기

for x in aa:
    if x.isdigit(): #isdecimal()
        res += x
    
    else: #연산자 처리
        if x=='(':
            stack.append(x)
        
        elif x==')': # 여는 괄호까지.
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.pop()
        
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res += stack.pop()
            stack.append(x)
        
        elif x == '+' or x=='-': #연산 후순위
            while stack and stack[-1]!='(': # 여는괄호 전까지만 !!!
                res += stack.pop()
            stack.append(x)

#stack에 남아있는 부분이 있을때
while stack:
    res += stack.pop()

print(''.join(map(str,res)))
