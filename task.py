import datetime


class task:
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