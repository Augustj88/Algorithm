#2022-03-29 제로

K=int(input())
N=[]
sum=0

for i in range(0,K):
    N.append(input())

for num in range(0,K-1):
    if int(N[num])==0:
        N.remove(N[num-1])
        N.remove(N[num])

for R in N:
    sum += int(R)

print(sum)
