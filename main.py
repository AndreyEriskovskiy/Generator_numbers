from random import uniform
from math import *


def get_ranges(amount_ranges, step):
    ranges = []
    for i in range(amount_ranges):
        min_border = round(i * step, 2)
        max_border = round(((i + 1) * step), 2)
        ranges.append((min_border, max_border))
    return ranges


def generate_number(lambda_):
    u = uniform(0.0, 1.0)  # Случайное число в интервале [0, 1)
    gen_digit = -log(1.0 - u) / lambda_
    return gen_digit


lambda_ = 4.6  # Интенсивность появления заявок
mew = 0.3  # Интенсивность обработки заявки
Tmax = 9.0  # Максимальное время моделирования
t = 0  # Текущее время

numbers = []
while t < Tmax:
    number = generate_number(lambda_)  # генерация числа
    numbers.append(number)
    t += 0.01  # Обновление текущего времени

amount_ranges = 20
step = 1 / amount_ranges
ranges = get_ranges(amount_ranges, step)  # полученные диапазоны
counter_digits_in_ranges = [0] * amount_ranges
for i in range(len(ranges)):
    min_border, max_border = min(ranges[i]), max(ranges[i])
    for j in range(len(numbers)):

        if min_border <= numbers[j] < max_border:
            counter_digits_in_ranges[i] += 1

numbers.sort(reverse=True)
print(f'Общее количество сгенерированных чисел: {len(numbers)}')

k = 0
for num in numbers:
    if num >= 1:
        k += 1

numbers = numbers[k:]

f = open('count_digits.txt', 'w')
f.close()
for i in range(len(ranges)):
    min_border, max_border = min(ranges[i]), max(ranges[i])
    print(
        f'Диапазон {i + 1} - [{min_border}, {max_border}) -- Количество чисел в диапазоне - {counter_digits_in_ranges[i]}')

print(f'Количество сгенерированных чисел, меньших 1: {len(numbers)}')
counter_digits_in_ranges = [str(num) + '\n' for num in counter_digits_in_ranges]
with open('count_digits.txt', 'a') as f:
    f.writelines(counter_digits_in_ranges)
