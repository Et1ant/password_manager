def get_master_password():
    attempts = 3
    while attempts > 0:
        password = input(f"Введите мастер-пароль (осталось попыток: {attempts}): ")
        if password == "1111":
            return True
        attempts -= 1
        print("Неверно!")
    return False
def add_password():
    service = input("Сервис: ")
    username = input("Логин: ")
    password = input("Пароль: ")
    with open("passwords.txt", "a") as file:
        file.write(f"{service} | {username} | {password}\n")
    print("Сохранено!")
def find_password():
    search = input("Какой сервис ищем?: ").lower()
    found = False
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                if search in line.lower():
                    print(f"Найдено: {line.strip()}")
                    found = True
        if not found:
            print("Ничего не нашлось.")
    except FileNotFoundError:
        print("База данных пуста.")
def delete_password():
    search = input("Запись для какого сервиса удалить?: ").lower()
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
        with open("passwords.txt", "w") as file:
            for line in lines:
                if search not in line.lower():
                    file.write(line)
        print("Готово (если такая запись была).")
    except FileNotFoundError:
        print("Файл еще не создан.")
if get_master_password():
    print("\nДобро пожаловать в систему!")
    while True:
        print("\n1. Добавить | 2. Найти | 3. Посмотреть все | 4. Удалить | 5. Выход")
        choice = input("Выбор: ")
        if choice == "1": add_password()
        elif choice == "2": find_password()
        elif choice == "3":
            with open("passwords.txt", "r") as f: print(f.read())
        elif choice == "4": delete_password()
        elif choice == "5": break
else:
    print("Доступ заблокирован.")