#오븐시계

H, M = map(int, input().split())
C = int(input())

if (M+C) > 59:
    newM = (M+C)%60
    newH = H + ((M+C)//60)
    if newH > 23:
        newH=newH-24
        print(newH, newM)
    else: print(newH, newM)

else:
    if H > 24:
        H = H-24
        print(H, M+C)
    else: print(H, M+C)