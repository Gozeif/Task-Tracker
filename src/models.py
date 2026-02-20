import datetime
import json

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        try:
            with open(self.filename, "r") as db:
                self.tasks = json.load(db)
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

class Task:
    statuses = ["todo", "in-progress", "done"]
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    def update_status(self, new_status):
        if new_status in self.statuses:
            self.status = new_status
            self.updatedAt = datetime.datetime.now()
        else:
            raise ValueError("Invalid status")
    def update_description(self, new_description):
        self.description = new_description
        self.updatedAt = datetime.datetime.now()