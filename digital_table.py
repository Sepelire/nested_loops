# Ввод: количество столбцов
#       количество линий
# Вывод: прямоугольник чисел по логике слева направо. Ряды выровнены
columns = int(input())
lines = int(input())
coun = 1
max_num = lines * columns
width = len(str(max_num))
for li in range(lines):
    for col in range(columns):
        print(f"{coun:>{width}}", end=" ")
        coun += 1
    print()
# 5
# 4
#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20