# Ввод: количество долек апельсина
# Вывод: вариации распределения этих долек на 3-их детей
cuss_ok = int(input())
print('А Б В')
for ch1 in range(1, cuss_ok - 1):
    for ch2 in range(1, cuss_ok - ch1):
        ch3 = cuss_ok - ch2 - ch1
        print (ch1, ch2, ch3)
# 4
# А Б В
# 1 1 2
# 1 2 1
# 2 1 1