import sys
input=sys.stdin.readline

N,M = map(int, input().split())
pokemons = {}
nums = {}
for i in range(1,N+1):
    aa = input().strip()
    pokemons[i]=aa
    nums[aa]=i
#nums = dict((v,k) for k,v in pokemons.items())

for i in range(M):
    quest = input().strip()
    if quest.isdigit():
        print(pokemons[int(quest)])
    else:
        print(nums[quest])




#시간초과 코드
# import sys
# input=sys.stdin.readline
# N,M = map(int, input().split())
# pokemon = []
# for _ in range(N):
#     pokemon.append(input().strip().lower())

# pok = dict(zip(range(1,N+1), map(str.lower, pokemon)))

# for i in range(M):
#     quest = input()
#     if quest.isdigit():
#         print(pok[int(quest)])
#     else:
#         print(dict((v,k) for k,v in pok.items()).get(quest))