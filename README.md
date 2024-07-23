To-Do List Application
This is a simple command-line To-Do List application written in Python. It allows users to add tasks, view tasks, mark tasks as done, and exit the application.

Features
Add a task
View all tasks
Mark a task as done
Exit the application
How to Use
Clone the repository:

Copy code
git clone https://github.com/Shaik-Nihal/todo-list-app.git
cd todo-list-app
Run the application:

Copy code
python Codsoft_Task_01.py
Follow the on-screen instructions:

Choose an option from the menu by entering the corresponding number.
Add tasks, view the list of tasks, mark tasks as done, or exit the application.
Menu Options
1. Add Task: Allows you to add a new task to the to-do list.
2. Show Tasks: Displays all the tasks with their current status (Done/Not Done).
3. Mark Task as Done: Marks a specified task as done.
4. Exit: Exits the application.
Code Overview
Class: ToDoList
Methods:
__init__(self): Initializes an empty list for tasks.
add_task(self, task): Adds a new task to the list.
view_tasks(self): Displays all tasks and their status.
mark_task_done(self, task_number): Marks a specified task as done.
exit_app(self): Exits the application.
Function: main()
The main function creates an instance of the ToDoList class and provides a menu for user interaction. It runs an infinite loop to accept user inputs until the user chooses to exit the application.
Example
Copy code
===== To-Do List =====
1. Add Task
2. Show Tasks
3. Mark Task as Done
4. Exit
Enter your choice: 1
Enter the task: Buy groceries
Task added!

===== To-Do List =====
1. Add Task
2. Show Tasks
3. Mark Task as Done
4. Exit
Enter your choice: 2

Tasks:
1. Buy groceries - Not Done


Feel Free to Contact
ni78ha34l8@gmail.com
