#2022-03-22 설탕공장

#상근이 'N'kg 배달 >> 사탕가게
#설탕공장의 설탕은 3kg, 5kg
#18kg배달시: 3kg*6개=18kg >> 상근 5kg*3개 + 3kg*1개 더 적은개수 배달
#'N'kg 배달시 봉지를 몇개 가져가면 되는지 구하기

n = int(input())
r = 0 #봉지수

while n >= 0: #설탕무게가 0보다 작거나 같을 때까지 반복
    if n % 5 == 0:
        new_r=r+(n//5)
        print(new_r)
        break
    n -= 3
    r += 1

else:
    print('-1')

