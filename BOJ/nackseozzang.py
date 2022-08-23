# 새싹이다
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \\. \". L_r\'')
print('   `~\\/')
print('      |')
print('      |')

import random

# # 코드를 작성하세요.
# cnt = 4
# num = random.randint(1, 20)

# while cnt > 0 :
#     answer = int(input('기회가 {0}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요 : '.format(cnt)))
#     if answer == num :
#         print('축하합니다. {0}번만에 숫자를 맞히셨습니다.'.format(cnt))
#         break
#     elif answer > num :
#         print('Down')
#         cnt -= 1
#     else :
#         print('Up')
#         cnt -= 1
        
# if cnt == 0:
#     print('아쉽습니다. 정답은 {0}였습니다.'.format(num))

# with open('vocabulary.txt', 'w', encoding='UTF-8') as f:
#     while True:
#         word_eng = input('영어 단어를 입력하세요: ')
#         if word_eng == 'q':
#             break
        
#         word_kor = input('한국어 뜻을 입력하세요: ')
#         if word_kor == 'q':
#             break
        
#         f.write('{0}: {1}\n'.format(word_eng, word_kor))


# vocab = {}
# with open('vocabulary.txt', 'r', encoding='UTF-8') as f :
#     for line in f:
#         data = line.strip().split(': ')
#         word_eng, word_kor = data[0], data[1]
#         vocab[word_eng] = word_kor

# # 목록 가져오기
# keys = list(vocab.keys())

# # 문제 내기
# while True:
#     # 랜덤 문제 받아오기
#     index = random.randint(0, len(keys)-1)
#     word_eng = keys[index]
#     word_kor = vocab[word_eng]

#     guess = input('{}: '.format(word_kor))

#     # 프로그램 끝내기
#     if guess == 'q':
#         break

#     if guess == word_eng:
#         print('정답입니다!\n')
#     else:
#         print('아쉽습니다. 정답은 {}입니다.\n'.format(word_eng))



# def generate_numbers(n):
#     arr = []
#     for i in range(n):
#         # arr.append(random.randint(1, 45))
#         num = random.randint(1, 45)
#         while num in arr:
#             num = random.randint(1, 45)
#         arr.append(num)
#     return arr

# def draw_winning_numbers():
#     g_nums = sorted(generate_numbers(6))
#     b_nums = generate_numbers(1)
#     return g_nums + b_nums

# def count_matching_numbers(list_1, list_2):
#     cnt = 0
#     for i in range(len(list_1)):
#         for j in range(len(list_2)):
#             if list_1[i] == list_2[j]:
#                 cnt += 1
#     return cnt

# def check(numbers, winning_numbers):
#     # 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
#     # 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
#     # 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
#     # 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
#     # 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)
#     count=0
#     special=0
#     result = 0
#     for i in range(len(numbers)):
#         for j in range(len(winning_numbers)):
#             if(numbers[i]==winning_numbers[j]):
#                 count+=1
#                 if(numbers[i] == winning_numbers[len(winning_numbers) - 1]):
#                     special += 1
#                     count -= 1
    
#     if count == 6:
#         result = 1000000000
#     elif count == 5 and special == 1:
#         result = 50000000
#     elif count == 5:
#         result = 1000000
#     elif count == 4:
#         result = 50000
#     elif count == 3:
#         result = 5000
#     else:
#         result = 0
#     return result

# numbers_test = generate_numbers(6)
# winning_numbers_test = draw_winning_numbers()
# print(numbers_test)
# print(winning_numbers_test)
# print(check(numbers_test, winning_numbers_test))




# z = x = ["이가훈", "김원일", "성재훈", "우설희", "최규호"]
# y = ["강귀윤", "김민주", "최고은", "우설희", "최규호"]

for i in range(3, 9, 2):
    print(i)