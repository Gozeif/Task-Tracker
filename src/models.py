from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4
from nanoid import generate


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

safe_alphabet = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

@dataclass
class Task:
    title: str
    # We use a factory for default values to ensure every task gets a unique ID and timestamp
    # generate an 8-character string directly; slicing isn't needed now that size matches
    id: str = field(default_factory=lambda: generate(safe_alphabet, size=8))
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