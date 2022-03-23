#2022-03-20 - 더하기 사이클

num=int(input("숫자를 입력하세요:"))
first_num = num
cnt=0
while True:
    
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b*10)+c

    cnt = cnt+1

    if (num == first_num):
        print(cnt)
        break