import os
from utils import clear_console, pause

def show_menu():
    while True:
        clear_console()
        print("--- Работа с файлами ---")
        print("1. Создать файл")
        print("2. Записать в файл строку")
        print("3. Прочитать файл")
        print("4. Удалить файл")
        print("5. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_to_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            return
        else:
            print("Неверный выбор, попробуйте снова.")
            pause()

def create_file():
    clear_console()
    filename = input("Введите имя файла: ").strip()
    
    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    try:
        open(filename, 'w').close()
        print(f"Файл {filename} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
    
    pause()

def write_to_file():
    clear_console()
    filename = input("Введите имя файла для записи: ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    if not os.path.exists(filename):
        print(f"Файл {filename} не существует.")
        pause()
        return

    try:
        with open(filename, 'a') as file:
            data = input("Введите строку для записи: ")
            file.write(data + "\n")
        print(f"Строка записана в файл {filename}.")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")
    
    pause()

def read_file():
    clear_console()
    filename = input("Введите имя файла для чтения: ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                print(f"Содержимое файла {filename}:")
                print(file.read())
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
    else:
        print(f"Файл {filename} не существует.")
    
    pause()

def delete_file():
    clear_console()
    filename = input("Введите имя файла для удаления: ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"Файл {filename} успешно удален.")
        except Exception as e:
            print(f"Ошибка при удалении файла: {e}")
    else:
        print(f"Файл {filename} не существует.")
    
    pause()
