from core import get_auth, get_marks, get_schedule_week, get_schedule_month, middlemark
from interface import get_user_credentials, print_marks, print_schedule

DEFAULT_LOGIN = "Kovla_ea99"
DEFAULT_PASSWORD = "sb8yLe5@"

def main():
    login = DEFAULT_LOGIN
    password = DEFAULT_PASSWORD

    if not login or not password:
        login, password = get_user_credentials()
        print(f"Используется введённый логин: {login}")
    else:
        print(f"Используется логин по умолчанию: {login}")

    print(f"Пароль: {password}")

    if get_auth(login, password):
        print("Аутентификация прошла успешно. Токен сохранен!")
        marks = get_marks()
        print_marks(marks)
        print(f"Средний балл: {middlemark():.2f}")
        schedule_week = get_schedule_week("2025-06-02")
        print("------")
        print("Расписание на неделю:")
        print_schedule(schedule_week)
        schedule_month = get_schedule_month("2025-06-01")
        print("------")
        print("Расписание на месяц:")
        print_schedule(schedule_month)
    else:
        print("Ошибка аутентификации. Проверьте логин и пароль.")

if __name__ == "__main__":
    main()