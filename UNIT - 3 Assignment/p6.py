
import os
import sys

print("File and Directory Operations")
print("1. Create Directory")
print("2. List Directory Contents")
print("3. Create File")
print("4. Write to File")
print("5. Read File")
print("6. Delete File")
print("7. Delete Directory")
print("8. Exit")

while True:
    choice = input("\nEnter your choice: ")

    if choice == '1':
        dirname = input("Enter directory name: ")
        os.makedirs(dirname, exist_ok=True)
        print("Directory created successfully.")

    elif choice == '2':
        dirname = input("Enter directory path: ")
        if os.path.isdir(dirname):
            print(os.listdir(dirname))
        else:
            print("Directory does not exist.")

    elif choice == '3':
        filename = input("Enter file name: ")
        with open(filename, 'w') as f:
            pass
        print("File created successfully.")

    elif choice == '4':
        filename = input("Enter file name: ")
        data = input("Enter text to write: ")
        with open(filename, 'w') as f:
            f.write(data)
        print("Data written successfully.")

    elif choice == '5':
        filename = input("Enter file name: ")
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                print("File contents:", f.read())
        else:
            print("File does not exist.")

    elif choice == '6':
        filename = input("Enter file name: ")
        if os.path.isfile(filename):
            os.remove(filename)
            print("File deleted successfully.")
        else:
            print("File does not exist.")

    elif choice == '7':
        dirname = input("Enter directory name: ")
        if os.path.isdir(dirname):
            os.rmdir(dirname)
            print("Directory deleted successfully.")
        else:
            print("Directory does not exist.")

    elif choice == '8':
        print("Program terminated.")
        sys.exit()

    else:
        print("Invalid choice. Please try again.")
