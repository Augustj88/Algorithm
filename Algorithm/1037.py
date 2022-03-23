#2022-03-23 약수

case = int(input())
cList = []

for i in range(case):
    a = int(input())
    cList.append(a)

print(max(cList)*min(cList))

#>>> 런타임에러로 코드수정
case = int(input())
a = list(map(int,input().split()))
print(max(a)*min(a))
