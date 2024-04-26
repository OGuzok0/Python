import requests

def update_student_info(student_id, updated_student_data):
    url = f"http://127.0.0.1:80/students/{student_id}"
    response = requests.put(url, json=updated_student_data)
    return response.json()

# Пример использования функции
student_id = 4
updated_data = {"name": "Новый Студент", "age": 23, "major": "Химия"}
response = update_student_info(student_id, updated_data)
print(response)
