# Ввод: количество линий
#       количество столбцов
# Вывод: прямоугольник чисел по логике слева направо и далее змейкой. Ряды выровнены
lines = int(input())
columns = int(input())
coun = 1
max_num = lines * columns
width = len(str(max_num))

for li in range(lines):
    if li % 2 == 0:
        for col in range(columns):
            print(f"{coun:>{width}}", end=" ")
            coun += 1
    else:
        coun += columns - 1
        for col in range(columns):
            print(f"{coun:>{width}}", end=" ")
            coun -= 1
        coun += columns + 1
    print()
# 5
# 4
#  1  2  3  4
#  8  7  6  5
#  9 10 11 12
# 16 15 14 13
# 17 18 19 20