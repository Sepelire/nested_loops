# Ввод: количество учатсников
# Вывод: отсчёт, с учётом того, что каждый последующий участник стартует на секунду позже
participants_count = int(input())
sec_until_start = 3
for participant in range(1, participants_count + 1):
    for sec in range(sec_until_start, 0, -1):
        print(f'До старта {sec} секунд(ы)')
    sec_until_start += 1
    print(f'Старт {participant}!!!')

# 2
# До старта 3 секунд(ы)
# До старта 2 секунд(ы)
# До старта 1 секунд(ы)
# Старт 1!!!
# До старта 4 секунд(ы)
# До старта 3 секунд(ы)
# До старта 2 секунд(ы)
# До старта 1 секунд(ы)
# Старт 2!!!