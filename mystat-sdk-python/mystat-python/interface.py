def get_user_credentials():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password

def print_marks(marks):
    print("Ваши оценки:")
    if not marks or not isinstance(marks, list):
        print("Нет данных.")
        return
    for item in marks:
        date = item.get("mark_date", "дата неизвестна")
        subject = item.get("name_spec", "Неизвестный предмет")
        mark = item.get("mark", "Нет оценки")
        teacher = item.get("fio_teach", "")
        theme = item.get("theme", "")
        print(f"{date} | {subject} | Оценка: {mark} | Преподаватель: {teacher} | Тема: {theme}")