a = ['Aditya', 'Saurabh', 'Rohit', 'Ankit', 'Rajat']

def registration():
    name = input("Enter your name: ")
    a.append(name)
    print("Registration successful!")

def list_names():
    print("Registered names:")
    for name in a:
        print(name)

def update():
    old_name = input("Enter the name to update: ")
    if old_name in a:
        new_name = input("Enter the new name: ")
        index = a.index(old_name)
        a[index] = new_name
        print("Update successful!")
    else:
        print("Name not found!")

def delete():
    delete_name = input("Enter the name to delete: ")
    if delete_name in a:
        a.remove(delete_name)
        print("Delete successful!")
    else:
        print("Enter the correct name")

def main():
    operations = {
        '1': registration,
        '2': list_names,
        '3': update,
        '4': delete
    }
    while True:
        print("\nChoose operation:")
        print("1. Register")
        print("2. List")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        operation = operations.get(choice)
        if operation:
            operation()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
