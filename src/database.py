import os
import psycopg as db
from src.models import Task, tasks
from src.config import Config

db_uri = Config.DB.uri

class LoadManager:
    @staticmethod
    def load_tasks():
        """Loads tasks from the database."""
        if not db_uri:
            print("DATABASE_URI environment variable not set.")
            return
        try:
            with db.connect(db_uri) as conn:
                with conn.cursor() as cursor:
                    # This ensures the table exists before we try to select from it.
                    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT, description TEXT, status TEXT, created_at TEXT, updated_at TEXT)")
                    cursor.execute("SELECT id, title, description, status, created_at, updated_at FROM tasks")
                    tasks = [Task(**data) for data in cursor.fetchall()]
        except db.Error as e:
            print(f"Database error during load: {e}")
        return tasks

    @staticmethod
    def save_tasks():
        """Saves tasks to the database."""
        if not db_uri:
            print("Database URI not set.")
            return
        try:
            # Use `with` for automatic connection and cursor closing
            with db.connect(db_uri) as conn:
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
                    for task in tasks:
                        # On conflict, we update existing tasks but preserve the original created_at timestamp.
                        cursor.execute(
                            # Using ON CONFLICT lets this handle both inserts and updates in one query but not deletions
                            # The EXCLUDED keyword refers to the row proposed for insertion, allowing us to update existing rows with new values while keeping created_at unchanged.
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

    def delete_task(task_id):
        """Deletes a task from the database."""
        if not db_uri:
            print("Database URI not set.")
            return
        try:
            with db.connect(db_uri) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        except db.Error as e:
            print(f"Database error during delete: {e}")