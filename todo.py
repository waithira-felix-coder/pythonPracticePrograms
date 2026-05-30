todo_list =[]

while True:
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task);
    elif choice == "2":
            print("\nTasks: ")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}.{task}")


    elif choice == "3":
            break
    else:
            print("Invalid choice")
