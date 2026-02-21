from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

@dataclass
class Task:
    title: str
    # We use a factory for default values to ensure every task gets a unique ID and timestamp
    id: str = field(default_factory=lambda: str(uuid4())[:8])
    description: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    status: Status = Status.TODO

    def to_dict(self):
        """Converts the object to a dictionary for JSON saving."""
        data = asdict(self)
        data["status"] = data["status"].value  # Convert enum to string value
        return data

    @classmethod
    def from_dict(cls, data):
        """Creates a Task object from a dictionary (loading from JSON)."""
        data["status"] = Status(data["status"])  # Convert string value back to enum
        return cls(**data)

# import datetime
# import json

# class TaskManager:
#     def __init__(self, filename="tasks.json"):
#         self.filename = filename
#         try:
#             with open(self.filename, "r") as db:
#                 self.tasks = json.load(db)
#         except FileNotFoundError:
#             self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)

#     def get_tasks(self):
#         return self.tasks

#     def save_tasks(self):
#         with open(self.filename, "w") as f:
#             json.dump(self.tasks, f, default=str)

# class Task:
#     statuses = ["todo", "in-progress", "done"]
#     def __init__(self, id, description, status, createdAt, updatedAt):
#         self.id = id
#         self.description = description
#         self.status = status
#         self.createdAt = createdAt
#         self.updatedAt = updatedAt
#     def update_status(self, new_status):
#         if new_status in self.statuses:
#             self.status = new_status
#             self.updatedAt = datetime.datetime.now()
#         else:
#             raise ValueError("Invalid status")
#     def update_description(self, new_description):
#         self.description = new_description
#         self.updatedAt = datetime.datetime.now()