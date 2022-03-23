N=int(input())
result=N

for i in range(N):
    word=input() #abab
    for a in range(len(word)-1): #4번반복
        if word[a] == word[a+1]: #만약 abab n번째 인덱스 글자가 다음인덱스 글자와 같다면 넘어간다.
            pass
        elif word[a] in word[a+1:]: #만약 abab 다음인덱스글자들 안에 n번째 글자가 있다면
            result-=1
            break
print(result)