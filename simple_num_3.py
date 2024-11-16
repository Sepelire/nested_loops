# Ввод: количество чисел
#       числа
# Вывод: количество простых чисел
n = int(input())
counter = 0
for i in range(n):
    num = int(input())
    flag = False
    if num == 1:
        continue
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            flag = True
            break
    if not flag:
        counter += 1
print(counter)
# 4
# 312
# 24
# 525
# 3
# 1