#2022-03-24 최대공약수와 최소공배수

#공약수: 두 개 이상의 자연수의 공통인 약수
#공배수: 두 개 이상의 자연수의 공통인 배수

#최대공약수=GCD
#최소공배수=LCM
#유클리드호제법 사용

A, B = map(int, input().split())
C = A*B
if A < B:
    a, b = B, A
elif A > B:
    a, b = A, B

R = a % b

while True:
    a = b
    b = R
    R = a % b
    if R == 0:
        print(b)
        print(C//b)
        break