from src.database import LoadManager
from src.models import Task, Status, tasks
from datetime import datetime


class TaskManager:
    @staticmethod
    def add_task(title, description=""):
        # let Task default_factory produce a unique id
        new_task = Task(title=title, description=description)
        tasks.append(new_task)
        LoadManager.save_tasks()

    @staticmethod
    def remove_task(task_id):
        for task in tasks:
            if task.id == task_id:
                tasks.remove(task)
                LoadManager.delete_task(task_id)
                return
        print(f"Task with ID {task_id} not found.")

    @staticmethod
    def update_task_title(task_id, new_title):
        for task in tasks:
            if task.id == task_id:
                task.title = new_title
                task.updated_at = datetime.now().isoformat()
                break
        LoadManager.save_tasks()

    @staticmethod
    def update_task_status(task_id, new_status):
        for task in tasks:
            if task.id == task_id:
                task.status = Status(new_status)
                task.updated_at = datetime.now().isoformat()
                break
        LoadManager.save_tasks()

    @staticmethod
    def update_task_description(task_id, new_description):
        for task in tasks:
            if task.id == task_id:
                task.description = new_description
                task.updated_at = datetime.now().isoformat()
                break
        LoadManager.save_tasks()