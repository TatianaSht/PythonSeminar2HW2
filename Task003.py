# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите число для границы интервала: "))
res_degree = 1
while res_degree <= number:
    print(res_degree, end=" ")
    res_degree *= 2
