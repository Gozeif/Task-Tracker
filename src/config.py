import os
from pathlib import Path
import sys
from dotenv import load_dotenv

# Load variables from .env if it exists (useful for local Windows dev)
load_dotenv()

class DatabaseConfig:
    # 1. Non-sensitive variables from .env
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_name = os.getenv("POSTGRES_DB_NAME", "task_tracker")
    db_host = os.getenv("DB_HOST", "localhost")  # 'db' inside Docker, 'localhost' on Windows
    db_port = os.getenv("DB_PORT", "5432")

    @property
    def db_pass(self):
        """
        Using a property means the password is only 
        fetched when you actually ask for it.
        """
        return Config.get_secret("db-pw", fallback_file="db_password.txt")

    @property
    def uri(self):
        return self.get_db_uri()

    def get_db_uri(self):
        """Construct the full database URI using the config values."""
        if not self.db_pass:
            return None
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

class AppConfig:
    def __init__(self):
        self.debug = os.getenv("DEBUG", "False").lower() == "true"
        self.port = int(os.getenv("APP_PORT", 8000))
        # If you later add email notifications:
        # EMAIL_SENDER = os.getenv("EMAIL_SENDER")

class Config:
    DB = DatabaseConfig()
    APP = AppConfig()
    @staticmethod
    def validate():
        """Checks if critical configurations are present before the app starts."""
        # 1. Check for the Database Password
        try:
            password = Config.DB.db_pass
            if not password:
                raise ValueError("Password is empty")
        except (FileNotFoundError, ValueError) as e:
            # If we are NOT in debug mode, crash the app with a clear error
            if not Config.APP.debug:
                print(f"CRITICAL ERROR: {e}")
                print("Production environment detected. Database secrets are required.")
                sys.exit(1)
            else:
                # In Debug/Windows mode, just print a warning
                print(f"WARNING: Database secret not found ({e}).")
                print("Debug mode detected. Ensure 'secrets/db_password.txt' exists.")
                if input("Do you want to continue without a database connection? (y/n): ").lower() == "y":
                    print("Continuing without database connection. Some features may not work.")
                else:
                    sys.exit(1)

    @staticmethod
    def get_secret(secret_name, default=None, fallback_file=None):
        """Unified helper for Docker secrets and local Windows fallbacks."""
        # 1. Check Docker Secrets
        docker_path = Path(f"/run/secrets/{secret_name}")
        if docker_path.exists():
            return docker_path.read_text().strip()
        # 2. Check Local Secrets folder (for Windows Dev)
        if fallback_file:
            local_path = Path(__file__).parent.parent / "secrets" / fallback_file
            if local_path.exists():
                return local_path.read_text().strip()
        # 3. Check Environment Variables
        return os.getenv(secret_name.upper(), default)