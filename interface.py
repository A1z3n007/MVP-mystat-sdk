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

def print_schedule(schedule):
    if not schedule or "data" not in schedule or not schedule["data"]:
        print("Нет данных.")
        return
    for lesson in schedule["data"]:
        date = lesson.get("date", "дата неизвестна")
        lesson_num = lesson.get("lesson", "")
        start = lesson.get("started_at", "")
        end = lesson.get("finished_at", "")
        subject = lesson.get("subject_name", "Неизвестный предмет")
        teacher = lesson.get("teacher_name", "")
        room = lesson.get("room_name", "")
        mark = lesson.get("mark", "")
        mark_str = f" | Оценка: {mark}" if mark is not None else ""
        print(f"{date} | Пара: {lesson_num} | {start}-{end} | {subject} | Преподаватель: {teacher} | Аудитория: {room}{mark_str}")