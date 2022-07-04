
# 1032 명령 프롬프트
N = int(input()) # N입력값
arr = list(input()) # 비교할 대상 list를 arr에 담기

for i in range(N-1): # 비교할 대상 arr리스트가 있으니 N-1만 돔
    arr2 = list(input()) # list입력

    for j in range(len(arr)): # arr의 길이만큼 돔
        if arr[j] != arr2[j]: # 대상 arr과 새로운 입력값 arr2과 비교
            arr[j] = '?' # 다르다면 -> "?" 출력

print(''.join(arr)) # arr 출력