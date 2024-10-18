import os
import zipfile
from utils import clear_console, pause

def show_menu():
    while True:
        clear_console()
        print("--- Работа с zip архивами ---")
        print("1. Создать zip архив")
        print("2. Добавить файл в zip архив")
        print("3. Разархивировать архив")
        print("4. Удалить архив")
        print("5. Назад в главное меню")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_zip_archive()
        elif choice == "2":
            add_file_to_zip()
        elif choice == "3":
            extract_zip()
        elif choice == "4":
            delete_zip()
        elif choice == "5":
            return
        else:
            print("Неверный выбор, попробуйте снова.")
            pause()

def create_zip_archive():
    clear_console()
    filename = input("Введите имя архива (без .zip): ") + ".zip"
    with zipfile.ZipFile(filename, 'w') as zipf:
        print(f"Архив {filename} создан.")
    pause()

def add_file_to_zip():
    clear_console()
    zip_filename = input("Введите имя архива (без .zip): ") + ".zip"
    file_to_add = input("Введите путь к файлу для добавления: ")

    if os.path.exists(file_to_add):
        with zipfile.ZipFile(zip_filename, 'a') as zipf:
            zipf.write(file_to_add, os.path.basename(file_to_add))
            print(f"Файл {file_to_add} добавлен в архив {zip_filename}.")
    else:
        print("Файл для добавления не существует.")
    pause()

def extract_zip():
    clear_console()
    zip_filename = input("Введите имя архива (без .zip): ") + ".zip"
    extract_path = input("Введите путь для разархивирования: ")

    if os.path.exists(zip_filename):
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(extract_path)
            print(f"Архив {zip_filename} распакован в {extract_path}.")
    else:
        print("Архив не существует.")
    pause()

def delete_zip():
    clear_console()
    filename = input("Введите имя архива (без .zip): ") + ".zip"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Архив {filename} удален.")
    else:
        print(f"Архив {filename} не существует.")
    pause()
