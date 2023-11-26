List = []
def display_list():
    if List:
        print("Items:")
        for index, item in enumerate(List, start=1):
            print(f"{index}. {item}")
    else:
        print("No items yet.")
def add_item():
    item = input("Enter the  item: ")
    List.append(item)
    print(f"{item} added to the  list.")
def remove_item():
    display_list()
    if List:
        try:
            index = int(input("Enter the index of the item to remove: "))
            if 0 <= index < len(List):
                removed_item = List.pop(index)
                print(f"Removed: {removed_item}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    else:
        print("No items to remove.")
while True:
    print("\nMenu:")
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        display_list()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
