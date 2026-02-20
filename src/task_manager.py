import json


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        try:
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, default=str)