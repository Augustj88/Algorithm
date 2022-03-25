#2022-03-22 - 달팽이는 올라가고 싶다.

a,b,v = map(int, input().split())
#소요일 = (전체길이-내려오는 길이)/(올라가는길이-내려오는길이=총 올라가는길이)
d=(v-b)/(a-b)

if d==int(d):print(int(d))
else: print(int(d)+1)

# 내장함수사용(math)
import math
print(math.ceil((v-b)/(a-b)))