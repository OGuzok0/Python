import random

def play_game(doors, trials):
    change_wins = 0
    stay_wins = 0

    for _ in range(trials):
        prize = random.randint(0, doors - 1)
        first_choice = random.randint(0, doors - 1)
        shown = random.choice([i for i in range(doors) if i != first_choice and i != prize])
        changed = random.choice([i for i in range(doors) if i != first_choice and i != shown])

        change_wins += changed == prize
        stay_wins += first_choice == prize

    return change_wins / trials, stay_wins / trials

doors = int(input("Сколько дверей: "))
trials = 10000

change_prob, stay_prob = play_game(doors, trials)
print(f"Вероятность победы при смене выбора: {change_prob:.4f}")
print(f"Вероятность победы при оставлении выбора: {stay_prob:.4f}")
