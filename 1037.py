

# 1037 약수

N = int(input()) # N입력값
num = list(map(int,input().split())) # list입력값

num.sort() # 오름차순 정렬

print(num[0]*num[-1]) # 첫값과 맨 끝값을 곱하면 배수가 된다.