# НОД с вводимым юзером количеством чисел
num_count = int(input())
nod = int(input())
for i in range(num_count - 1):
    n = int(input())
    while nod != n:
        if nod > n:
            nod -= n
        else:
            n -= nod
print(nod)
# 3
# 102
# 39
# 768