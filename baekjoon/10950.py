#A+B-3

T=int(input())
C=[]
for i in range(T):
    A,B=map(int,input().split())
    C.append(A+B)

for c in C:
    print(c)