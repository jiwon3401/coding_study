#[#Q4. 후위식 연산(스택)]
'''
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
'''

aa = input()
stack = []
for i in aa:
    if i.isdecimal():
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i=='+':
            tmp = b+a
        elif i=='-':
            tmp = b-a
        elif i=='*':
            tmp = b*a
        elif i=='/':
            tmp = b/a
        stack.append(tmp)
print(stack[0])


#sol 
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack[0])
