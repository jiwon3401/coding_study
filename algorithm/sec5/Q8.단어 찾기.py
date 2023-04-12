#[#Q8.단어 찾기]
'''
현수는 영어로 시를 쓰는 것을 좋아합니다. 현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다. 여러분이 찾아 주세요.
첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.
첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.
'''
import sys 
input = sys.stdin.readine
N = int(input())
word_dict = dict()
for _ in range(N):
    word = input()
    word_dict[word] = 0
for _ in range(N-1):
    word = input()
    word_dict[word]=1
print(word_dict)

not_word = {v:k for k,v in word_dict.items()}
print(not_word.get(0))
