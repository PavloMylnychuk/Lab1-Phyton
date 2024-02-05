import math

# Введення значення m
m = float(input("Введіть значення m: "))

# Обчислення значення функції z
z = 1 / (math.sqrt(m) + math.sqrt(2))

# Виведення результату
print("Значення z:", z)
# Завдання 2.1: Визначити, чи є n простим числом.
n = int(input("Введіть число n: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} є простим числом.")
else:
    print(f"{n} не є простим числом.")


# Завдання 3.1: Знайти мінімальний від'ємний елемент.
array = [int(x) for x in input("Введіть елементи масиву через пробіл: ").split()]

negative_elements = [num for num in array if num < 0]

if negative_elements:
    min_negative = min(negative_elements)
    print("Мінімальний від'ємний елемент:", min_negative)
else:
    print("В масиві немає від'ємних елементів.")

# Завдання 3.2: Обчислити суму парних елементів масиву.
sum_even = sum(num for num in array if num % 2 == 0)
print("Сума парних елементів масиву:", sum_even)

# Завдання 3.3: Вивести масив на екран у зворотному порядку.
reversed_array = array[::-1]
print("Масив у зворотному порядку:", reversed_array)
