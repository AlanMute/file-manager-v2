import os
from utils import clear_console, pause

def show_menu():
    while True:
        clear_console()
        print("--- Работа с XML файлами ---")
        print("1. Создать XML файл вручную")
        print("2. Прочитать XML файл")
        print("3. Удалить XML файл")
        print("4. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_xml_file_manual()
        elif choice == "2":
            read_xml_file()
        elif choice == "3":
            delete_xml_file()
        elif choice == "4":
            return
        else:
            print("Неверный выбор, попробуйте снова.")
            pause()

def create_xml_file_manual():
    clear_console()
    filename = input("Введите имя XML файла (без .xml): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".xml"

    # Создаем пустую мапу (словарь) для хранения тегов и их значений
    data = {}
    while True:
        tag = input("Введите тег (оставьте пустым для завершения): ").strip()
        if not tag:
            break
        value = input(f"Введите значение для тега <{tag}>: ")
        data[tag] = value

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Записываем вручную заголовок и корневой элемент
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<root>\n')

            # Записываем теги и их значения из мапы
            for tag, value in data.items():
                file.write(f"  <{tag}>{value}</{tag}>\n")

            # Закрываем корневой элемент
            file.write('</root>\n')
        
        print(f"Файл {filename} создан вручную.")
    except Exception as e:
        print(f"Ошибка при создании XML файла: {e}")
    
    pause()

def read_xml_file():
    clear_console()
    filename = input("Введите имя XML файла (без .xml): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".xml"

    if os.path.exists(filename):
        try:
            # Чтение содержимого файла и вывод его на экран
            with open(filename, 'r', encoding='utf-8') as file:
                print(f"Содержимое файла {filename}:")
                print(file.read())  # Выводим содержимое файла как текст
        except Exception as e:
            print(f"Ошибка при чтении XML файла: {e}")
    else:
        print(f"Файл {filename} не существует.")
    
    pause()

def delete_xml_file():
    clear_console()
    filename = input("Введите имя XML файла (без .xml): ").strip()

    if not filename:
        print("Имя файла не может быть пустым. Попробуйте снова.")
        pause()
        return

    filename += ".xml"

    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"Файл {filename} успешно удален.")
        except Exception as e:
            print(f"Ошибка при удалении XML файла: {e}")
    else:
        print(f"Файл {filename} не существует.")
    
    pause()
