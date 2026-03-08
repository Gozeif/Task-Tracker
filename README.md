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

### Git Clone


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

### Docker Setup

#### Building and running your application

Start the application by running docker compose in the project root folder:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

#### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

#### References
* [Docker's Python guide](https://docs.docker.com/language/python/)

## Configuration

The application stores data in a postgresql database.
config.py looks for the database password as a docker secret, and fallsback to an environment variable if not found.

## Usage

Run the main script to interact with the tracker:

```bash
python main.py
```

The CLI will prompt for commands such as `add`, `list`, `update`, and `delete`. Follow on-screen instructions.

## Project Structure

```
Task Tracker/
├── db/                   # SQL database schema and migrations
│   └── init.sql          # Database schema initialization
├── src/                  # Core application logic
│   ├── config.py         # Secret & Env loading logic
│   ├── database.py       # Persistence layer
│   ├── logic.py          # Business rules
│   ├── main.py           # CLI entry point
│   └── models.py         # Data classes
├── compose.yaml          # Multi-container orchestration
├── Dockerfile            # App image configuration
├── requirements.txt      # App dependencies
└── README.md             # You are here
```

Created as a solution for the [Task Tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).