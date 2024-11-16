# Ввод: количество чисел
#       числа
# Вывод: количество чисел палиндромов
n = int(input())
pal = 0
for p in range(n):
    num = int(input())
    orig_num = num
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    if orig_num == rev_num:
        pal += 1
print(pal)
# 5
# 123
# 321
# 323
# 434
# 567
# 2