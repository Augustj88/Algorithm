#2022-03-21/단어공부
import collections #Counter사용을 위한 모듈 임포트

user = (input('영단어를 입력하시오:').replace(' ','')).upper() #replace-공백제거
Ulist=[] #빈리스트 생성

cnt = collections.Counter(user) #입력값 카운트(key:value)
max_value = max(list(cnt.values())) #value의 max값


for i in list(cnt.keys()): #키값 리스트로 나열 key=i
    if cnt[i] == max_value: #키값과 밸류값이 같다면
        Ulist.append(i) #key를 Ulist에 저장한다.

if len(Ulist) > 1: #list의 길이가 1보다 많다면 '?'출력
    print('?')
else:
    print(''.join(Ulist)) #리스트를 문자열로 반환 / 대문자로 출력

