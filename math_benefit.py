n = int(input())
addition_n = 0      
decimal_sum = 0
max_sum = 0
max_base = 2
for base in range(2, 11):
    temp = n
    current_sum = 0
    while temp > 0:                                 
        current_sum += temp % base   
        temp //= base             
    if max_sum < current_sum or (max_sum == current_sum and base < max_base):
        max_sum = current_sum
        max_base = base
print(max_base) 
