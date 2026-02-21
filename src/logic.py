from src.database import LoadManager
from src.models import Task, Status
from datetime import datetime

class TaskManager:
    def __init__(self):
        # create a LoadManager instance responsible for persistence
        self.manager = LoadManager()
        self.tasks = self.manager.tasks

    def add_task(self, title, description=""):
        # let Task default_factory produce a unique id
        new_task = Task(title=title, description=description)
        self.tasks.append(new_task)
        self.manager.save_tasks()

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.manager.tasks = self.tasks
        self.manager.save_tasks()

    def update_task_title(self, task_id, new_title):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                task.updated_at = datetime.now().isoformat()
                break
        self.manager.tasks = self.tasks
        self.manager.save_tasks()

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = Status(new_status)
                task.updated_at = datetime.now().isoformat()
                break
        self.manager.tasks = self.tasks
        self.manager.save_tasks()

    def update_task_description(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                task.updated_at = datetime.now().isoformat()
                break
        self.manager.tasks = self.tasks
        self.manager.save_tasks()

    def get_tasks(self):
        return self.tasks