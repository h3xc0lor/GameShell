import random

def play_game():
    choices = ['камень', 'ножницы', 'бумага']

    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Выберите свой ход: камень, ножницы или бумага. Для выхода наберите 'выход'.")

    while True:
        player_choice = input("Ваш выбор: ").lower()

        if player_choice == 'выход':
            print("Спасибо за игру!")
            break

        if player_choice not in choices:
            print("Неверный ввод! Попробуйте еще раз.")
            continue

        computer_choice = random.choice(choices)

        print("Ваш выбор:", player_choice)
        print("Выбор компьютера:", computer_choice)

        if player_choice == computer_choice:
            print("Ничья! Оба выбрали", player_choice)
        elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
             (player_choice == 'ножницы' and computer_choice == 'бумага') or \
             (player_choice == 'бумага' and computer_choice == 'камень'):
            print("Вы победили! {} побеждает {}".format(player_choice, computer_choice))
        else:
            print("Вы проиграли! {} побеждает {}".format(computer_choice, player_choice))

play_game()
