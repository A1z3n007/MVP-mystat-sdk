import requests
import json

def get_auth(login, password):
    url = "https://mapi.itstep.org/v1/mystat/auth/login"
    payload = {
        "login": login,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        token = response.text.strip()
        if token:
            with open("token.txt", "w") as f:
                f.write(token)
            return True
        else:
            print("Ответ сервера пуст.")
            return False
    else:
        print("Ошибка! Код ответа:", response.status_code)
        print("Текст ответа:", response.text)
        return False

def get_token():
    try:
        with open("token.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Токен не найден. Сначала выполните вход.")
        return None

def get_marks():
    token = get_token()
    if not token:
        return None
    url = "https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            return response.json()
        except Exception:
            print("Ошибка при разборе ответа сервера!")
            print("Текст ответа:", response.text)
            return None
    else:
        print("Ошибка! Код ответа:", response.status_code)
        print("Текст ответа:", response.text)
        return None

def get_schedule_week(date):
    token = get_token()
    if not token:
        print("Токен недействителен, требуется повторная авторизация.")
        return None
    url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=week&date_filter={date}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка получения расписания: {response.status_code} — {response.text}")
        return None

def get_schedule_month(date):
    token = get_token()
    if not token:
        print("Токен недействителен, требуется повторная авторизация.")
        return None
    url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=month&date_filter={date}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка получения расписания: {response.status_code} — {response.text}")
        return None

def middlemark():
    marks = get_marks()
    if not marks:
        return 0
    # Если marks — список словарей, ищем ключ 'mark'
    mark_values = []
    for item in marks:
        try:
            mark = float(item.get("mark", 0))
            mark_values.append(mark)
        except Exception:
            continue
    if not mark_values:
        return 0
    return sum(mark_values) / len(mark_values)