
# 1110 더하기 사이클

N = int(input())
num = N # 사이클 돌려야할 신규값으로 처음만 N값을 넣어준다.
cnt = 0 # count출력값

while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b*10)+c

    cnt += 1

    if num == N: # num과 N이 같다면 while문 종료
        break
print(cnt)

# if문을 while문 첫부분에 넣어주면 안된다.
# Why?
# 첫 문장에 넣을 시 while문이 돌지 않고 바로 종료됨