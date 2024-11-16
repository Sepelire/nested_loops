# Ввод: высота и ширина числового квадрата
# Вывод: числовой квадрат. Столбцы одинаковой ширины
n = int(input())
max_number = ''
for i in range(n):
    for j in range(n):
        next_number = min(i, j, n - i - 1, n - j - 1) + 1
        if len(max_number) < len(str(next_number)):
            max_number = str(next_number)
len_number = len(max_number)
for i in range(n):
    for j in range(n):
        result = min(i, j, n - i - 1, n - j - 1) + 1
        print(f'{result: >{len_number}}', end=' ')
    print()
# 5
# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1