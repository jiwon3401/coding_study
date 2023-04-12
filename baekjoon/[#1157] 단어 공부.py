#1157 
'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

words = input().upper()

word_dict = {}
for w in words:
    if w in word_dict:
        word_dict[w] += 1
    else:
        word_dict[w] = 1
        
max_list = []
for key, value in word_dict.items():
    if value == max(word_dict.values()):
        max_list.append(key)
        
if len(max_list)>=2:
    print('?')
else:
    print(max_list[0])