# На столе лежат n монеток. Некоторые из них лежат вверх  решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное  количество монет,
# которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0
# 2

count = int(input("Введите число монет: "))
head = 0
tails = 0
for i in range(count):
    coin = int(input(f"Введите число стороны для {i + 1}-й монеты, 1 - орел, 0 - решка: "))
    if coin == 1:
        head += 1
    if coin == 0:
        tails += 1
if head + tails == count:
    if head <= tails:
        print(f"Нужно перевернуть {head} шт.")
    if tails < head:
        print(f"Нужно перевернуть {tails} шт.")
else:
    print("Введены некорректные данные!")
