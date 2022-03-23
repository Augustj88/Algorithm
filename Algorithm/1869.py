#2022-03-22 달팽이는 올라가고 싶다.

a,b,v = map(int, input().split())
#소요일 =
d=(v-b)/(a-b)
if d==int(d):print(int(d))
else: print(int(d)+1)