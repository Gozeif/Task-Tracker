import os

def get_secret(secret_name, default=None):
    """Helper to read Docker secrets or environment variables."""
    secret_path = f"/run/secrets/{secret_name}"
    if os.path.exists(secret_path):
        with open(secret_path, "r") as f:
            return f.read().strip()
    return os.getenv(secret_name.upper(), default)

# Load variables once
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASS = get_secret("DB_PW", "devpass")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "myapp_db")

# Construct the full connection string
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"