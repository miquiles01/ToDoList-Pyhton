class ToDoList:
    def __init__(self, file_name='tasks.txt'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                tasks = [task.strip() for task in file.readlines()]
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            self.save_tasks()
        else:
            print("Número de tarefa inválido.")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa na lista.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()
