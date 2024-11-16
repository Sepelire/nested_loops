# Ввод: количество детей
# Вывод: число ребёнка раскладывается на цифры, и находится максимальное из них
# далее идёт конкатенация с максимальной цифрой в числе следующего ребёнка
n = int(input())
big_number = ''
for i in range(n):
    max_digit = 0
    child_number = int(input())
    while child_number > 0:
        current_digit = child_number % 10
        if max_digit < current_digit:
            max_digit = current_digit
        child_number //= 10
    big_number += str(max_digit)
print(big_number)
# 2
# 123
# 234
# 34