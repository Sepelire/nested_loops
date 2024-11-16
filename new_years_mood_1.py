# выводит ёлку из числа, выровненную по левому краю
n = int(input())
counter = 1
row = 1
while counter <= n:
    for i in range(row):
        if counter <= n:
            print(f'{counter}', end=' ')
        counter += 1
    print('')
    row += 1

# 6
# 1
# 2 3
# 4 5 6