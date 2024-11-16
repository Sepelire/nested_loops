# Ввод: размер таблицы
#       ширина столбцов
# Вывод: таблица умножения с разделителями. Столбцы одинаковой ширины
table_size = int(input())
spaces = int(input())
division = '|'
max_size = table_size * spaces + table_size - 1
for i in range(1, table_size + 1):
    counter = 0
    for j in range(1, table_size * 2):
        if j % 2 != 0 and j != table_size * 2 - 1:
            counter += 1
            print(f'{i * counter: ^{spaces}}', end='')
        elif j == table_size * 2 - 1:
            counter += 1
            print(f'{i * counter: ^{spaces}}')
        elif j % 2 == 0:
            print(division, end='')
    if i != table_size:
        print('-' * max_size)
# 3
# 5
#   1  |  2  |  3
# -----------------
#   2  |  4  |  6
# -----------------
#   3  |  6  |  9