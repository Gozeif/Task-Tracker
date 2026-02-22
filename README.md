# Task Tracker
A simple Python command-line application for managing a task list stored in JSON.
This project provides basic create/read/update/delete operations on tasks and persists them in a file under `data/tasks.json`.

## Features

- Add, edit, delete, and list tasks
- Task persistence using a JSON datastore
- Structured code with separate modules for database access, business logic, and models

## Prerequisites

- Python 3.10 or newer
- A virtual environment (recommended)

## Setup

1. Clone the repository if you haven't already:
   ```bash
   git clone https://github.com/Gozeif/Task-Tracker.git "Task Tracker"
   cd "Task Tracker"
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application stores data in `data/tasks.json`. The repository includes a template file which will be created automatically when the first task is added.

## Usage

Run the main script to interact with the tracker:

```bash
python -m src.main
```

The CLI will prompt for commands such as `add`, `list`, `update`, and `delete`. Follow on-screen instructions.

## Project Structure

```
README.md
requirements.txt
TODO.txt
data/
    tasks.json
src/
    database.py   # persistence layer
    logic.py      # business rules
    main.py       # CLI entry point
    models.py     # data classes for tasks
```

Created as a solution for the [Task Tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).