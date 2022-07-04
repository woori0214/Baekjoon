# 1157 단어 공부

arr = input()
check = [0]*26

for i in arr:
    if i >= 'A' and i <= 'Z':
        check[ord(i)-65]+=1 # 대문자 A-Z
    else:
        check[ord(i)-97]+=1 # 소문자 a-z

max_check = max(check) # 알파벳 값 중 최댓값
res = [] # 결과값을 넣을 리스트

for i in check: # check를 돌면서 최댓값 확인 후 결과값 넣기
    if i == max_check:
        res.append(i)

if len(res) != 1: # 최댓값이 여러개면 ? 출력
    print("?")
else: # 아니면 대문자 값 출력
    print(chr(check.index(max_check)+65))
