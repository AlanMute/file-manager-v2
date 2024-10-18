import json
import os
from utils import clear_console, pause

def show_menu():
    while True:
        clear_console()
        print("--- Работа с JSON файлами ---")
        print("1. Создать JSON файл")
        print("2. Создать объект и сериализовать в JSON")
        print("3. Прочитать JSON файл")
        print("4. Удалить JSON файл")
        print("5. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_json_file()
        elif choice == "2":
            create_and_serialize_object()
        elif choice == "3":
            read_json_file()
        elif choice == "4":
            delete_json_file()
        elif choice == "5":
            return
        else:
            print("Неверный выбор, попробуйте снова.")
            pause()

def create_json_file():
    clear_console()
    filename = input("Введите имя JSON файла (без .json): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".json"
    data = {}
    while True:
        key = input("Введите ключ (оставьте пустым для завершения): ")
        if key == "":
            break
        value = input(f"Введите значение для ключа {key}: ")
        data[key] = value

    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Файл {filename} создан.")
    except Exception as e:
        print(f"Ошибка при создании JSON файла: {e}")
    
    pause()

def create_and_serialize_object():
    clear_console()
    filename = input("Введите имя JSON файла для объекта (без .json): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".json"

    try:
        data = {
            "name": input("Введите имя: "),
            "age": int(input("Введите возраст: ")),
            "city": input("Введите город: "),
            "is_student": input("Вы студент? (y/n): ").lower() == 'y'
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Объект сериализован и записан в файл {filename}.")
    except ValueError:
        print("Ошибка: возраст должен быть числом.")
    except Exception as e:
        print(f"Ошибка при сериализации объекта в JSON: {e}")

    pause()

def read_json_file():
    clear_console()
    filename = input("Введите имя JSON файла (без .json): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".json"
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                print(f"Содержимое файла {filename}:")
                print(json.dumps(data, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            print(f"Ошибка: файл {filename} содержит некорректный JSON.")
        except Exception as e:
            print(f"Ошибка при чтении файла {filename}: {e}")
    else:
        print(f"Файл {filename} не существует.")
    
    pause()

def delete_json_file():
    clear_console()
    filename = input("Введите имя JSON файла (без .json): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".json"
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"Файл {filename} удален.")
        except Exception as e:
            print(f"Ошибка при удалении файла {filename}: {e}")
    else:
        print(f"Файл {filename} не существует.")
    
    pause()
