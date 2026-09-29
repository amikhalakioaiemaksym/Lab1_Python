import math

# Завдання 1. Обчислення значення функції z(m)
print("=== Завдання 1 ===")
m = float(input("Введіть значення m: "))

if m == 3:
    print("Помилка: ділення на нуль (m не може дорівнювати 3).")
elif (m + 3) / (m - 3) < 0:
    print("Помилка: вираз під квадратним коренем від'ємний.")
else:
    z = math.sqrt((m + 3) / (m - 3))
    print(f"Значення z({m}) = {z:.4f}")


# Завдання 2. Обчислення добутку: 2 * 4 * 6 * ... * (2 * n)
print("\n=== Завдання 2 ===")
n = int(input("Введіть натуральне число n: "))

if n <= 0:
    print("Помилка: n має бути натуральним числом (n > 0).")
else:
    product = 1
    for i in range(1, n + 1):
        product *= 2 * i
    print(f"Результат обчислення добутку для n = {n}: {product}")


# Завдання 3. Обробка одновимірного масиву
print("\n=== Завдання 3 ===")
N = int(input("Введіть кількість елементів масиву N: "))

arr = []
print(f"Введіть {N} цілих чисел (по одному в рядок):")
for i in range(N):
    arr.append(int(input(f"Елемент [{i}]: ")))

print(f"\nВведений масив: {arr}")

negative_elements = [x for x in arr if x < 0]
if negative_elements:
    min_neg = min(negative_elements)
    print(f"1. Мінімальний від'ємний елемент: {min_neg}")
else:
    print("1. Від'ємні елементи в масиві відсутні.")

even_sum = sum(x for x in arr if x % 2 == 0)
print(f"2. Сума парних елементів масиву: {even_sum}")

odd_elements = [x for x in arr if x % 2 != 0]
reversed_odds = odd_elements[::-1]
print(f"3. Непарні елементи у зворотному порядку: {reversed_odds}")

input("\nНатисніть Enter, щоб закрити програму...")