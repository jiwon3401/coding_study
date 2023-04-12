#10809
'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오. 
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
'''


from string import ascii_lowercase
alpha = list(ascii_lowercase)
word = list(input())

for i in range(len(alpha)):
    if alpha[i] in word:
        alpha[i] = word.index(alpha[i])
        print(alpha[i], end=' ')
    else:
        alpha[i] = -1
        print(alpha[i], end=' ')
