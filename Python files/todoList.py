class todoList   : 
    TodoList ="TodoList"
    def __init__(self):
        self.tasks =[]


    def add_task(self):
        task = input("Enter a task: ")
        self.task.append({"task": task, "done": False})
        print("Task added!")

    def view_task(self):
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{1}. {task['task']} - {status}")

    def delete_task(self):
        self.view_tasks()
        task_num = int(input("Enter task number to delete: ")) -1
        try:
            del self.tasks[task_num]
            print("Task deleted!")
        except IndexError:
            print("Invalid task number!")

    def mark_done(self):
        self.view_tasks()
        task_num = int(input("Enter task number to mark as done: ")) -1
        try:
            self.tasks[task_num]["done"] = True
            print("Task marked as done!")
        except IndexError:
            print("Invalid task number!")

    def main():
        todo = todoList()
        while True:
            print("\n1. Add Task")
            print("\n2. View Task")
            print("\n3. Delete Task")
            print("\n4. Mark Task as Done")
            print("5. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                todo.add_task()
            elif choice =="2":
                todo.view_task()
            elif choice =="3":
                todo.delete_task()
            elif choice == "4":
                todo.mark_done()
            elif choice == "5":
                break
            else:
                print("Invalid option!")

if __name__ == "__main__":
         main()
