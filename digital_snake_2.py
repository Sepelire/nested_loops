# Ввод: количество линий
#       количество столбцов
# Вывод: прямоугольник чисел по логике сверху вниз и далее змейкой. Ряды выровнены
lines = int(input())
columns = int(input())
max_number = lines * columns
width = len(str(max_number))
for li in range(lines):
    for col in range(columns):
        if col % 2 == 0:
            counter = col * lines + li + 1
        else:
            counter = (col + 1) * lines - li
        print(f'{counter:>{width}}', end=' ')
    print()
# 4
# 5
#  1  8  9 16 17
#  2  7 10 15 18
#  3  6 11 14 19
#  4  5 12 13 20