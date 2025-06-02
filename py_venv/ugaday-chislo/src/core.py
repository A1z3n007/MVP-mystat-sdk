import random
from config import ОТ, ДО

def generate_random_number():
    return random.randint(ОТ, ДО)

def check_guess(guess, number):
    if guess < number:
        return "Слишком низко!"
    elif guess > number:
        return "Слишком высоко!"
    else:
        return "Поздравляем! Вы угадали число!"

def play_game():
    number_to_guess = generate_random_number()
    attempts = 0
    print(f"Я загадал число от {ОТ} до {ДО}. Попробуйте угадать!")

    while True:
        try:
            user_guess = int(input("Введите ваше число: "))
            attempts += 1
            result = check_guess(user_guess, number_to_guess)
            print(result)
            if result == "Поздравляем! Вы угадали число!":
                print(f"Вы угадали число за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")