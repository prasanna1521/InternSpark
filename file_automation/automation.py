import os
import shutil
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def rename_files(directory):
    for count, filename in enumerate(os.listdir(directory), start=1):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            new_name = f"report{count}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
    print(Fore.GREEN + "✔ Files renamed successfully." + Style.RESET_ALL)

def sort_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1][1:].lower()
            if ext:
                folder = os.path.join(directory, ext.capitalize())
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, filename))
    print(Fore.GREEN + "✔ Files sorted successfully." + Style.RESET_ALL)

def clean_empty_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for d in dirs:
            folder_path = os.path.join(root, d)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
    print(Fore.GREEN + "✔ Empty folders cleaned successfully." + Style.RESET_ALL)

def main():
    print(Fore.CYAN + "Welcome to File Automation Project" + Style.RESET_ALL)
    print("Choose an operation:")
    print("1. Rename Files")
    print("2. Sort Files")
    print("3. Clean Empty Folders")

    choice = input("Enter choice (1/2/3): ")
    directory = input("Enter directory path: ")

    if not os.path.exists(directory):
        print(Fore.RED + f"❌ Error: The directory '{directory}' does not exist." + Style.RESET_ALL)
        return

    if choice == "1":
        rename_files(directory)
    elif choice == "2":
        sort_files(directory)
    elif choice == "3":
        clean_empty_folders(directory)
    else:
        print(Fore.YELLOW + "⚠ Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
