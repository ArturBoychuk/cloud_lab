def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")
    return a / b

def main():
    print("Вітаємо в калькуляторі!")
    print("Оберіть операцію:")
    print("1. Додати")
    print("2. Відняти")
    print("3. Помножити")
    print("4. Поділити")

    operation = input("Введіть номер операції (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))

        if operation == '1':
            print("Результат:", add(a, b))
        elif operation == '2':
            print("Результат:", subtract(a, b))
        elif operation == '3':
            print("Результат:", multiply(a, b))
        elif operation == '4':
            print("Результат:", divide(a, b))
    else:
        print("Невірний вибір операції. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
