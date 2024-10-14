def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Основна частина програми
n = int(input("Введіть номер числа Фібоначчі: "))

if n < 0:
    print("Число повинно бути додатнім.")
else:
    print(f"Число Фібоначчі номер {n} дорівнює {fibonacci(n)}")