def reverse_number(num):
    return int(str(num)[::-1])

if __name__ == "__main__":
    try:
        test_number = int(input("Введите число, которое хотите перевернуть: "))
        print("Перевёрнутое число:", reverse_number(test_number))
    except ValueError:
        print("Ошибка: Нужно ввести целое число.")
