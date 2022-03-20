#20220320

case=int(input('케이스의 수를 입력:'))

for i in range(case):
    cnt=0
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0] #학생수 제외한 나머지를 학생수로 나누어 평균

    for s in scores[1:]: #한 케이스의 점수들을 반복문
        if s > avg: #평균값보다 점수가 높다면
            cnt+=1
    
    per = (cnt/scores[0])*100 #백분율환산
    print('%.3f' %per + '%')#소수점 3개까지만 출력