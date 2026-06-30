import os
import logging

# Configure logging
logging.basicConfig(filename="logs.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def rename_files(directory, prefix):
    try:
        for count, filename in enumerate(os.listdir(directory)):
            old_path = os.path.join(directory, filename)
            if os.path.isfile(old_path):
                new_name = f"{prefix}_{count}{os.path.splitext(filename)[1]}"
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                logging.info(f"Renamed: {filename} → {new_name}")
        print("✅ Files renamed successfully.")
    except Exception as e:
        logging.error(f"Error renaming files: {e}")
        print(f"❌ Error: {e}")

def sort_files(directory):
    try:
        for filename in os.listdir(directory):
            file_ext = os.path.splitext(filename)[1][1:]
            if file_ext:
                folder_path = os.path.join(directory, file_ext)
                os.makedirs(folder_path, exist_ok=True)
                os.rename(os.path.join(directory, filename),
                          os.path.join(folder_path, filename))
                logging.info(f"Moved: {filename} → {folder_path}")
        print("✅ Files sorted successfully.")
    except Exception as e:
        logging.error(f"Error sorting files: {e}")
        print(f"❌ Error: {e}")

def clean_empty_folders(directory):
    try:
        for folder in os.listdir(directory):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path) and not os.listdir(folder_path):
                os.rmdir(folder_path)
                logging.info(f"Deleted empty folder: {folder_path}")
        print("✅ Empty folders cleaned.")
    except Exception as e:
        logging.error(f"Error cleaning folders: {e}")
        print(f"❌ Error: {e}")

def main():
    print("📂 File Automation Script")
    directory = input("Enter directory path: ").strip()
    print("Choose an operation:\n1. Rename Files\n2. Sort Files\n3. Clean Empty Folders")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        prefix = input("Enter prefix for renaming: ")
        rename_files(directory, prefix)
    elif choice == "2":
        sort_files(directory)
    elif choice == "3":
        clean_empty_folders(directory)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
