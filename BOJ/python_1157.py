S = input().upper()
new_S = list(set(S)) # 중복 제거

cnt = [] # 문자 개수 체크

for i in new_S:
    count = S.count(i) # 원래 문자열에서 문자 개수 체크
    cnt.append(count)

if cnt.count(max(cnt)) >= 2: # 문자의 max 개수가 2개 이상있다면
    print('?')
else: # 최대 개수가 하나만 있다면
    print(new_S[cnt.index(max(cnt))])