import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print(f"Ошибка {response.status_code} при получении данных.")
    return None

def get_students_list():
    return fetch_data("http://127.0.0.1:80/students")

# Функция для получения информации о конкретном студенте по его номеру
def get_student_info(student_id):
    return fetch_data(f"http://127.0.0.1:80/students/{student_id}")

print("Список студентов:")
students_list = get_students_list()
if students_list:
    print(students_list)

print("\nИнформация о студенте с номером 1:")
student_info = get_student_info(1)
if student_info:
    print(student_info)
