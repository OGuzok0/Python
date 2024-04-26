import requests

# Функция для добавления нового студента на сервер
def add_student(student_data):
    url = "http://127.0.0.1:80/students"
    response = requests.post(url, json=student_data)
    return response.json()

# Пример использования функции
new_student_data = {"id": 4, "name": "Новый Студент", "age": 22, "major": "Биология"}
response = add_student(new_student_data)
print(response)
