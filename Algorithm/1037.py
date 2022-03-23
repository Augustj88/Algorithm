#2022-03-23 약수

case = int(input())
cList = []

for i in range(case):
    a = int(input())
    cList.append(a)

print(max(cList)*min(cList))
