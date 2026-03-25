import json
import os
import requests

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
SAVE_FILE = "save.json"

def load_exchange_rates():
    response = requests.get(URL)
    data = response.json()
    return data['Valute']

def show_all_currencies(valutes):
    for code, info in valutes.items():
        print(f"{code}: {info['Name']} - {info['Value']} RUB")

def show_currency(valutes, code):
    val = valutes.get(code.upper())
    if val:
        print(f"{code.upper()}: {val['Name']} - {val['Value']} RUB")
    else:
        print("Валюта с таким кодом не найдена.")

def load_groups():
    if not os.path.exists(SAVE_FILE):
        return {}
    with open(SAVE_FILE, 'r') as f:
        return json.load(f)

def save_groups(groups):
    with open(SAVE_FILE, 'w') as f:
        json.dump(groups, f, indent=2, ensure_ascii=False)

def show_groups(groups):
    if not groups:
        print("Группы валют не созданы.")
    for group_name, currencies in groups.items():
        print(f"Группа '{group_name}': {', '.join(currencies)}")

def add_currency_to_group(groups, group_name, currency_code, valutes):
    if currency_code.upper() not in valutes:
        print("Такой валюты нет в курсе.")
        return
    if group_name not in groups:
        groups[group_name] = []
    if currency_code.upper() in groups[group_name]:
        print("Валюта уже в группе.")
    else:
        groups[group_name].append(currency_code.upper())
        print(f"Валюта {currency_code.upper()} добавлена в группу '{group_name}'.")

def remove_currency_from_group(groups, group_name, currency_code):
    if group_name in groups and currency_code.upper() in groups[group_name]:
        groups[group_name].remove(currency_code.upper())
        print(f"Валюта {currency_code.upper()} удалена из группы '{group_name}'.")
    else:
        print("Валюта или группа не найдены.")

def main():
    valutes = load_exchange_rates()
    groups = load_groups()

    while True:
        print("\nВыберите действие:")
        print("1. Показать все курсы валют")
        print("2. Показать курс валюты по коду")
        print("3. Показать все группы валют")
        print("4. Создать/Добавить валюту в группу")
        print("5. Удалить валюту из группы")
        print("6. Сохранить группы")
        print("7. Загрузить группы")
        print("0. Выход")

        cmd = input("Введите номер действия: ").strip()

        if cmd == "1":
            show_all_currencies(valutes)

        elif cmd == "2":
            code = input("Введите код валюты: ").strip()
            show_currency(valutes, code)

        elif cmd == "3":
            show_groups(groups)

        elif cmd == "4":
            group_name = input("Введите имя группы: ").strip()
            currency_code = input("Введите код валюты: ").strip()
            add_currency_to_group(groups, group_name, currency_code, valutes)

        elif cmd == "5":
            group_name = input("Введите имя группы: ").strip()
            currency_code = input("Введите код валюты: ").strip()
            remove_currency_from_group(groups, group_name, currency_code)

        elif cmd == "6":
            save_groups(groups)
            print("Группы сохранены.")

        elif cmd == "7":
            groups = load_groups()
            print("Группы загружены.")

        elif cmd == "0":
            print("Выход из программы.")
            break

        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()