from core import play_game
from config import ОТ, ДО

def main():
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадаю число от {ОТ} до {ДО}.")
    play_game()

if __name__ == "__main__":
    main()