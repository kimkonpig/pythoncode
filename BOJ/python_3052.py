# array = []
# for i in range(0, 10):
#     array.append(int(input()) % 42)

# print(len(set(array)))

## 위 코드를 짧게 쓰면
array = [int(input())%42 for i in range(10)]
print(len(set(array)))