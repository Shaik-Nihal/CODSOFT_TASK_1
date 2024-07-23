class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print("Task added!")

    def view_tasks(self):
        print("\nTasks:")
        for index, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")

    def mark_task_done(self, task_number):
        task_index = task_number - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    def exit_app(self):
        print("Exiting the To-Do List.")
        exit()

def main():
    todo_list = ToDoList()
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_done(task_number)
        elif choice == '4':
            todo_list.exit_app()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()