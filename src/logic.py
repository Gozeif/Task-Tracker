from database import load_tasks, save_tasks
from models import Task, Status
from datetime import datetime
import uuid

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, description):
        new_task = Task(id=str(uuid.uuid4()), description=description)
        self.tasks.append(new_task)
        save_tasks(self.tasks)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        save_tasks(self.tasks)

    def update_task_title(self, task_id, new_title):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                task.updated_at = datetime.now().isoformat()
                break
        save_tasks(self.tasks)

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = Status(new_status)
                task.updated_at = datetime.now().isoformat()
                break
        save_tasks(self.tasks)

    def update_task_description(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                task.updated_at = datetime.now().isoformat()
                break
        save_tasks(self.tasks)

    def get_tasks(self):
        return self.tasks