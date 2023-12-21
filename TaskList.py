Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class TaskList:
...     def __init__(self):
...         self.tasks = []
...     def add_task(self, task):
...         self.tasks.append(task)
...         print(f"Task '{task}' added successfully.")
...     def remove_task(self, task):
...         if task in self.tasks:
...             self.tasks.remove(task)
...             print(f"Task '{task}' removed successfully.")
...         else:
...             print(f"Task '{task}' not found.")
...     def show_tasks(self):
...         if self.tasks:
...             print("Your Tasks:")
...             for idx, task in enumerate(self.tasks, start = 1):
...                 print(f"{idx}. {task}")
...         else:
...             print("No tasks available.")
... 
...             
>>> task_list = TaskList()
>>> task_list.show_tasks()
No tasks available.
>>> task_list.add_task("Complete homework")
Task 'Complete homework' added successfully.
>>> task_list.add_task("Buy groceries")
Task 'Buy groceries' added successfully.
>>> task_list.show_tasks()
Your Tasks:
1. Complete homework
2. Buy groceries
>>> task_list.remove_task("Buy groceries")
Task 'Buy groceries' removed successfully.
>>> task_list.show_tasks()
Your Tasks:
1. Complete homework
