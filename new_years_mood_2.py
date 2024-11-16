# Ввод: Размер ёлочки
# Вывод: Ёлочка выравненная по центру
n = int(input())
counter = 1
row = 1
longest_row = ''
while counter <= n:
    low_row = ''
    for i in range(row):
        if counter <= n:
            low_row += ' ' + str(counter)
        if len(low_row) > len(longest_row):
            longest_row = low_row
        counter += 1
    row += 1
width = len(longest_row)
counter = 1
row = 1
while counter <= n:
    current_row = ''
    for i in range(row):
        if counter <= n:
            current_row += str(counter) + ' '
        counter += 1
    print(f'{current_row: ^{width}}', end=' ')
    print()
    row += 1

# 14
#      1
#     2 3
#    4 5 6
#  7 8 9 10
# 11 12 13 14