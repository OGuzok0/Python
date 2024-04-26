import random

# Список предметов разных качеств
items = {
    "Обычный": ["Стальной меч", "Кожаная броня", "Деревянный щит", "Железные наручи", "Железные сапоги"],
    "Редкий": ["Огненный посох", "Кольчуга здоровья", "Эликсир маны"],
    "Эпический": ["Молот грома", "Кольцо неуязвимости", "Скрипучий трезубец"],
    "Легендарный": ["Меч вечности", "Драконья доспехи"]
}

# Шансы на выпадение предметов
chances = {"Обычный": 0.7, "Редкий": 0.2, "Эпический": 0.1, "Легендарный": 0.05}

def open_lootbox():
    loot = []
    for _ in range(20):
        for quality, chance in chances.items():
            if random.random() < chance:
                loot.append((quality, random.choice(items.get(quality, items["Обычный"]))))
                break
    return loot

# Получение списка полученных предметов
loot_results = open_lootbox()

# Подсчет количества предметов разных качеств
loot_counts = {quality: sum(1 for q, _ in loot_results if q == quality) for quality in items}

# Проверка на удачу
luck_message = ""
if loot_counts.get("Эпический", 0) > 3:
    luck_message += "Удача! "
if loot_counts.get("Легендарный", 0) > 1:
    luck_message += "Большая удача! "

# Форматированный вывод результатов
for quality, count in loot_counts.items():
    color = {"Обычный": "\033[0m", "Редкий": "\033[94m", "Эпический": "\033[95m", "Легендарный": "\033[93m"}.get(quality, "")
    print(f"{quality}: {color}{count}\033[0m")

print(luck_message)

# Вывод списка полученных предметов с подсветкой разных цветов
print("\nСписок полученных предметов:")
for quality, item in loot_results:
    color = {"Обычный": "\033[0m", "Редкий": "\033[94m", "Эпический": "\033[95m", "Легендарный": "\033[93m"}.get(quality, "")
    print(f"{color}{item}\033[0m")
