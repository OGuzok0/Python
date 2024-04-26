import requests

def delete_student(student_id):
    url = f"http://127.0.0.1:80/students/{student_id}"
    response = requests.delete(url)
    return response.json()

# Пример использования функции
student_id = 4
response = delete_student(student_id)
print(response)
