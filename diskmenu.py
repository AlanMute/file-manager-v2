import os
import shutil
from utils import clear_console, pause

def get_windows_drives():
    """Получение списка логических дисков на Windows."""
    drives = []
    bitmask = os.popen('wmic logicaldisk get name').read().splitlines()
    for line in bitmask:
        if ':' in line:
            drives.append(line.strip())
    return drives

def get_unix_drives():
    """Получение списка точек монтирования на Linux/macOS."""
    drives = []
    with open('/proc/mounts', 'r') as f:
        for line in f:
            if line.startswith('/dev/'):
                mount_point = line.split()[1]
                drives.append(mount_point)
    return drives

def show_disk_info():
    clear_console()
    print("--- Информация о дисках ---")
    
    if os.name == 'nt':  # Windows
        drives = get_windows_drives()
    else:
        drives = get_unix_drives()

    if not drives:
        print("Не удалось найти диски.")
    else:
        for drive in drives:
            try:
                total, used, free = shutil.disk_usage(drive)
                print(f"Диск {drive}")
                print(f"  Общий размер: {total // (2**30)} ГБ")
                print(f"  Использовано: {used // (2**30)} ГБ")
                print(f"  Свободно: {free // (2**30)} ГБ\n")
            except FileNotFoundError:
                print(f"Не удалось получить информацию для {drive}")
    
    pause()

