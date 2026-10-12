
import shutil
import os

print("File Operations Using shutil Module")
print("1. Copy File")
print("2. Move File")
print("3. Delete File")
print("4. Exit")

while True:
    choice = input("\nEnter your choice: ")

    if choice == '1':
        src = input("Enter source file path: ")
        dest = input("Enter destination path: ")

        if os.path.isfile(src):
            shutil.copy(src, dest)
            print("File copied successfully.")
        else:
            print("Source file does not exist.")

    elif choice == '2':
        src = input("Enter source file path: ")
        dest = input("Enter destination path: ")

        if os.path.isfile(src):
            shutil.move(src, dest)
            print("File moved successfully.")
        else:
            print("Source file does not exist.")

    elif choice == '3':
        filename = input("Enter file path to delete: ")

        if os.path.isfile(filename):
            os.remove(filename)
            print("File deleted successfully.")
        else:
            print("File does not exist.")

    elif choice == '4':
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
