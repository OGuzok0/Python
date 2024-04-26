import random

def catch_ball():
    return random.random() < 0.7  # 70% вероятность

# Список вопросов
questions = [
    "Какой ваш любимый цвет?",
    "Какое ваше любимое животное?",
    "В какой стране вы хотели бы жить?",
    "Какой ваш любимый фильм?",
    "Что вы обычно завтракаете?",
    "Какой у вас любимый музыкальный жанр?",
    "Какой последний книгу вы прочитали?",
    "Какой ваш любимый спорт?",
    "Какой у вас любимый вид искусства?",
    "Какое ваше хобби?"
]

# Список случайных ответов
random_answers = [
    "Синий",
    "Кот",
    "Франция",
    "Звездные войны",
    "Тосты с авокадо",
    "Рок",
    "Гарри Поттер",
    "Футбол",
    "Живопись",
    "Фотография"
]

# Список для истории игры
history = []

# Основной цикл игры
for i in range(10):
    question = random.choice(questions)

    # Ход компьютера
    computer_answer = random.choice(random_answers)
    history.append(("Компьютер", question, computer_answer))

    # Ваш ход
    user_answer = input(f"Вопрос: {question}\nВаш ответ: ")
    history.append(("Вы", question, user_answer))
    print()

# Вывод истории игры
print("\nИстория игры:")
for turn, question, answer in history:
    print(f"{turn} на вопрос '{question}' ответил: {answer}")
