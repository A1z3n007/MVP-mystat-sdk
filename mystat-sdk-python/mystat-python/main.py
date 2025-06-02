from core import get_auth, get_marks
from interface import get_user_credentials, print_marks

DEFAULT_LOGIN = "Kovla_ea99"
DEFAULT_PASSWORD = "sb8yLe5@"

def main():
    login = DEFAULT_LOGIN
    password = DEFAULT_PASSWORD

    if not login or not password:
        login, password = get_user_credentials()

    if get_auth(login, password):
        print("Аутентификация прошла успешно. Токен сохранен!")
        marks = get_marks()
        print_marks(marks)
    else:
        print("Ошибка аутентификации. Проверьте логин и пароль.")

if __name__ == "__main__":
    main()