import json
import os
from src.models import Task

class LoadManager:
    filename: str = "data/tasks.json"
    def __init__(self):
        self.tasks = self.load_tasks()
        print(f"Loaded {len(self.tasks)} tasks from {self.filename}")

    def save_tasks(self):
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename))
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)


    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]