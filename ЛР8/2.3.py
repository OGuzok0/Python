def reverse_number(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    numbers_input = input("Введите список чисел, разделённых пробелом: ")
    try:
        numbers = list(map(int, numbers_input.split()))
        for number in numbers:
            reversed_number = reverse_number(number)
            print(f"Оригинальное число: {number}, Перевёрнутое число: {reversed_number}")
            if is_palindrome(number):
                print(f"Число {number} является палиндромом.")
    except ValueError:
        print("Ошибка: Все элементы списка должны быть целыми числами.")
