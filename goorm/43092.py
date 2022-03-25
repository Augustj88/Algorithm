#리그경기횟수구하기

n = int(input())

#method1
cnt = 0
if n < 2: #예외처리
    print()
else:
    for i in range(1,n):
        cnt += i
    print(cnt)

#method2
def a():
    cnt = 0
    if n < 2:
        print()
    else:
        for i in range(1,n):
            cnt += i
        return cnt
print(a())
