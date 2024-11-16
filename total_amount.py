# Сумма введёных чисел. Сначала вводится количество чисел, а потом цифры, которые будут складываться
# Числа разлагаются на цифры, и только после этого ссумируются
num_count = int(input())
amount = 0
for i in range(num_count):
    num = int(input())
    while num > 0:
        amount += num % 10
        num //= 10
print(amount)
# 3
# 45
# 3
# 1
# 13