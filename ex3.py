import os
import sys
from colorama import init, Fore

init(autoreset=True)

def visualize_directory_structure(directory, indent=""):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(Fore.RED + f"Директорії {directory} не існує.")
        return

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(Fore.GREEN + f"{indent}├── Директорія: {item}")
            visualize_directory_structure(item_path, indent + "│   ")
        else:
            print(Fore.WHITE + f"{indent}└── Файл: {item}")


if len(sys.argv) != 2:
    print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
else:
    directory_path = sys.argv[1]
    visualize_directory_structure(directory_path)