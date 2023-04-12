#[Q3.뮤직비디오(결정알고리즘)]
'''
지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지되어야 한다. 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다. 
즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야한다. 또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 이 사업에 낭비되는 DVD를 가급적 줄이려고 한다. 
고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기로 하였다. 이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 그리고 M개의 DVD는
모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.
'''

import sys 
input = sys.stdin.readline 
N,M = map(int, input().split())
sl = list(map(int, input().split()))
        
start = max(sl)
end = sum(sl)
res = 0   
while start <= end:
    mid = (start + end)//2
    cnt = 1 #각 dvd 갯수
    sum_dvd = 0 #dvd 하나에 누적

    for i in sl:
        if sum_dvd + i > mid: #용량 초과
            cnt += 1 #새로운 dvd 만듦
            sum_dvd = i #새로운 dvd에서의 누적 시간
        else: 
            sum_dvd += i #기존 dvd에 추가 가능  
                  
    if cnt <= M:
        res = mid
        end = mid - 1
    elif cnt < N:
        start = mid +1

print(res)