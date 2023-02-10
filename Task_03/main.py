# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

numberNatural = int(input('Введите натуральное число: -> '))
degree = 0
res = 0
while res < numberNatural:
    res = 2 ** degree
    degree += 1
    if res < numberNatural:
        print(res)
        
    

    
    