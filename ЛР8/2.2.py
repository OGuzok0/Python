def is_palindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    try:
        test_number = int(input("Введите число, чтобы проверить, является ли оно палиндромом: "))
        print("Является палиндромом:", is_palindrome(test_number))
    except ValueError:
        print("Ошибка: Нужно ввести целое число.")
