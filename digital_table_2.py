# Ввод: количество линий
#       количество столбцов
# Вывод: прямоугольник чисел по логике сверху вниз. Ряды выровнены
lines = int(input())
columns = int(input())
max_num = lines * columns
width = len(str(max_num))
for li in range(lines):
    for col in range(columns):
        num = col * lines + li + 1
        print(f"{num:>{width}}", end=" ")
    print()
# 5
# 4
#  1  6 11 16
#  2  7 12 17
#  3  8 13 18
#  4  9 14 19
#  5 10 15 20