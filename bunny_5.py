# Выводит количество "зон"(циклов), в которых есть "зайка"(указанное слово)
n = int(input())
area_count = 0
bunny_in_area = 0
while area_count < n:
    flag = 0
    text = ''
    while text != 'ВСЁ':
        text = input()
        if text == 'зайка':
            flag = 1
    bunny_in_area += flag
    area_count += 1
print(bunny_in_area)

# 4
# зайка
# березка
# ВСЁ
# зайка
# зайка
# ВСЁ
# березка
# елочка
# березка
# ВСЁ
# елочка
# елочка
# елочка
# ВСЁ

# 2