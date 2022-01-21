H,M=map(int,input().split())
if M<=44:
    NH=H-1
    if H==0:
        NH=23
    print(NH,M+15)
elif M>=45:
    print(H,M-45)
