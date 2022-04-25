#빠른 A+B
import sys

T=int(sys.stdin.readline())
N=[sys.stdin.readline().strip() for i in range(T)]

for t in range(T):
    A,B=map(int,input().split())
    N.append(A+B)

for n in N:
    print(n)