import sys

while True:
    # Запрашиваем ввод для x
    while True:
        try:
            x = int(input("x: "))
            break  # Если ввод корректен, выходим из цикла
        except ValueError:
            print("Error: invalid literal for x, please enter a valid integer.")

    # Запрашиваем ввод для y и обрабатываем деление
    while True:
        try:
            y = int(input("y: "))
            result = x / y  # Проверяем деление на ноль
            break  # Если деление корректно, выходим из цикла
        except ValueError:
            print("Error: invalid literal for y, please enter a valid integer.")
        except ZeroDivisionError:
            print("Error: cannot divide by zero. Please enter a different value for y.")

    # Выводим результат
    print(f"{x} / {y} = {result}")
