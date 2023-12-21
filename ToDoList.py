class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully")
    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (Done)"
            print("Task marked as done.")
        else:
            print("Invalid task index.")
    def show_tasks(self):
        if self.tasks:
            for idx, task in enumerate(self.tasks, start = 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks available.")
todo_list = ToDoList()
todo_list.show_tasks()
todo_list.add_task("Complete project remainder")
todo_list.add_task("Do Workout")
todo_list.show_tasks()
todo_list.mark_task_done(0)
todo_list.show_tasks()
    