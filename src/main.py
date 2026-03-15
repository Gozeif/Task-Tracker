import typer
from rich.console import Console
from rich.table import Table
import src.logic as logic
from src.models import Status, tasks
from src.database import LoadManager

LoadManager.load_tasks(
app = typer.Typer(help="My Professional Task Tracker CLI application.")
console = Console()

@app.command()
def add(title: str, description: str = ""):
    """Add a new task with the given title and optional description."""
    logic.TaskManager.add_task(title, description)
    console.print(f"Task added: {title}", style="green")

@app.command()
def remove(task_id: str):
    """Remove a task by its ID."""
    logic.TaskManager.remove_task(task_id)
    console.print(f"Task removed: {task_id}", style="red")

@app.command()
def update(command: str,task_id: str, option: str):
    """Update a task's title by its ID."""
    if command == "title":
        logic.TaskManager.update_task_title(task_id, option)
        for task in logic.TaskManager.tasks:
            if task.id == task_id:
                console.print(f"Task title updated: {task.id}, {task.title}, {task.description}, {task.status.value}, {task.updated_at}, {task.created_at}", style="yellow")
                break
    elif command == "status":
        try:
            logic.TaskManager.update_task_status(task_id, option)
        except ValueError:
            console.print(
                f"'{option}' is not a valid status. "
                f"Choose from {[s.value for s in Status]}.",
                style="red",
            )
            return
        for task in tasks:
            if task.id == task_id:
                console.print(f"Task status updated: {task.id}, {task.title}, {task.description}, {task.status.value}, {task.updated_at}, {task.created_at}", style="yellow")
                break
    elif command == "description":
        logic.TaskManager.update_task_description(task_id, option)
        for task in tasks:
            if task.id == task_id:
                console.print(f"Task description updated: {task.id}, {task.title}, {task.description}, {task.status.value}, {task.updated_at}, {task.created_at}", style="yellow")
                break
    else:
        console.print("Invalid update command. Use 'title', 'status', or 'description'.", style="red")

@app.command()
def list(status: str = "all"):
    """Filter tasks by status if a specific status is provided; otherwise, list all tasks."""
    if status not in ["all", "todo", "in-progress", "done"]:
        console.print("Invalid list status. Use 'all', 'todo', 'in-progress', or 'done'.", style="red")
        return
    elif status != "all":
        """List tasks filtered by status."""
        tasks_filtered_by_status = [task for task in tasks if task.status.value == status]
    else:
        """List all tasks."""
        tasks_filtered_by_status = tasks
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="yellow")
    table.add_column("Status", style="green")
    table.add_column("Created At", style="blue")
    table.add_column("Updated At", style="blue")

    for task in tasks_filtered_by_status:
        table.add_row(task.id, task.title, task.description, task.status.value, task.created_at, task.updated_at)

    console.print(table)

if __name__ == "__main__":
    app()