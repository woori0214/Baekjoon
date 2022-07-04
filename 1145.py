
# 1145 적어도 대부분의 배수

arr = list(map(int, input().split())) # 리스트입력값
num = min(arr) # 리스트 숫자들 중 최솟값을 num에 대입

while True:
    cnt = 0 # count 값 reset

    for i in arr: # arr리스트를 돌면서 약수가 있다면 count++
        if num % i == 0:
            cnt+=1

    if cnt >= 3: # 문제에서 3개 이상이 될 시 중단이였으니 cnt를 3회 이상으로 조건을 검
        print(num)
        break
    num +=1