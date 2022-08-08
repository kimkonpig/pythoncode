def d(n):
    lst = list(map(int, str(n)))
    rst = n
    for i in lst:
        rst += i
    return rst

rst_list = [0 for i in range(1, 10036)]
for i in range(1,10036):
    func_rst = d(i)
    if func_rst <= 10000:
        rst_list[func_rst] += 1

for i in range(1, 10001):
    if rst_list[i] < 1:
        print(i)