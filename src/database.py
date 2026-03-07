import os
import psycopg as db
from src.models import Task
from src.config import DATABASE_URL

class LoadManager:
    def __init__(self):
        self.tasks = self.load_tasks()
        print(f"Loaded {len(self.tasks)} tasks from the database.")

    def save_tasks(self):
        if not DATABASE_URL:
            print("DATABASE_URL environment variable not set.")
            return
        try:
            # Use `with` for automatic connection and cursor closing
            with db.connect(DATABASE_URL) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tasks (
                            id TEXT PRIMARY KEY, 
                            title TEXT, 
                            description TEXT, 
                            status TEXT, 
                            created_at TEXT, 
                            updated_at TEXT
                        )
                    """)
                    for task in self.tasks:
                        # On conflict, we update existing tasks but preserve the original created_at timestamp.
                        cursor.execute(
                            """
                            INSERT INTO tasks (id, title, description, status, created_at, updated_at) 
                            VALUES (%s, %s, %s, %s, %s, %s) 
                            ON CONFLICT (id) DO UPDATE SET 
                                title = EXCLUDED.title, 
                                description = EXCLUDED.description, 
                                status = EXCLUDED.status, 
                                updated_at = EXCLUDED.updated_at
                            """,
                            (task.id, task.title, task.description, task.status.value, task.created_at, task.updated_at)
                        )
        except db.Error as e:
            print(f"Database error: {e}")

    def load_tasks(self):
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            print("DATABASE_URL environment variable not set.")
            return []
        
        tasks = []
        try:
            with db.connect(db_url) as conn:
                with conn.cursor() as cursor:
                    # This ensures the table exists before we try to select from it.
                    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT, description TEXT, status TEXT, created_at TEXT, updated_at TEXT)")
                    cursor.execute("SELECT id, title, description, status, created_at, updated_at FROM tasks")
                    for record in cursor.fetchall():
                        task_data = dict(zip(('id', 'title', 'description', 'status', 'created_at', 'updated_at'), record))
                        tasks.append(Task.from_dict(task_data))
        except db.Error as e:
            print(f"Database error during load: {e}")
        return tasks