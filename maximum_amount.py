# Ввод: количество детей
# Вывод: Победитель определяется путём сложения цифр в числе каждого ребёнка. У кого больше итог - тот и победил
n = int(input())
max_number = 0
for i in range(n):
    amount = 0
    child_name = input()
    child_number = int(input())
    while child_number > 0:
        amount += child_number % 10
        child_number //= 10
    if amount >= max_number:
        max_number = amount
        best_child = child_name
print(best_child)
# 3
# Vasya
# 12
# Petya
# 9
# Olya
# 11111
# Petya