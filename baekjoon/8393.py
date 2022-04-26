#합

n=int(input())
P=[]
ranN=0
for i in range(n+1):
    P.append(i)

for p in P:
    ranN += p

print(ranN)