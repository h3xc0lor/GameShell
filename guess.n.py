import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        guess = int(input("Введи свое предположение: "))
        attempts += 1

        if guess < secret_number:
            print("Больше!")
        elif guess > secret_number:
            print("Меньше!")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
            break

guess_number()
