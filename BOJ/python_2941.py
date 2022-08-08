alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in alphabet_list:
    s = s.replace(i, '*')

print(len(s))

# # 이렇게 쉬운데.. 난 정말 멍청하군