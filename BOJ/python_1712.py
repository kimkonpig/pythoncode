A, B, C = map(int, input().split())

# A : 고정비용, B : 가변비용, C : 노트북 가격
if B>=C: # A+(B*i) = C*i 일 때 수입=비용이므로 B>=C일때 손익분기점이 나타나지 않음, 먼저 걸름
    print(-1)
else:
    print(A//(C-B)+1)