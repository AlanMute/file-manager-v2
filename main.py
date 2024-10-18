import sys
import filemenu
import jsonmenu
import xmlmenu
import zipmenu
import diskmenu
from utils import clear_console

def main_menu():
    while True:
        clear_console()
        print("\n--- Главное меню ---")
        print("1. Информация о логических дисках")
        print("2. Работа с файлами")
        print("3. Работа с JSON файлами")
        print("4. Работа с XML файлами")
        print("5. Работа с zip архивами")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            diskmenu.show_disk_info()
        elif choice == "2":
            filemenu.show_menu()
        elif choice == "3":
            jsonmenu.show_menu()
        elif choice == "4":
            xmlmenu.show_menu()
        elif choice == "5":
            zipmenu.show_menu()
        elif choice == "6":
            print("Выход из программы.")
            sys.exit(0)
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()
