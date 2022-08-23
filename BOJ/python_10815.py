N = int(input())
cards = set(map(int, input().split()))
M = int(input())
valiCards = list(map(int, input().split()))

for i in valiCards:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")