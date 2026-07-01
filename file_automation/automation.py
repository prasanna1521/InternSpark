import os
import shutil

def rename_files(directory):
    for count, filename in enumerate(os.listdir(directory), start=1):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            new_name = f"report{count}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
    print("✔ Files renamed successfully.")

def sort_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1][1:].lower()
            if ext:
                folder = os.path.join(directory, ext.capitalize())
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, filename))
    print("✔ Files sorted successfully.")

def clean_empty_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for d in dirs:
            folder_path = os.path.join(root, d)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
    print("✔ Empty folders cleaned successfully.")

def main():
    print("Welcome to File Automation Project")
    print("Choose an operation:")
    print("1. Rename Files")
    print("2. Sort Files")
    print("3. Clean Empty Folders")

    choice = input("Enter choice (1/2/3): ")
    directory = input("Enter directory path: ")

    if choice == "1":
        rename_files(directory)
    elif choice == "2":
        sort_files(directory)
    elif choice == "3":
        clean_empty_folders(directory)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
