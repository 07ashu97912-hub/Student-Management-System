import json
from pathlib import Path
from .models import Student

class StudentStorage:
    def __init__(self, filename="data/students.json"):
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        if not self.filename.exists():
            self.save_all([])

    def load_all(self):
        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return [Student.from_dict(item) for item in data]
        except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
            return []

    def save_all(self, students):
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in students], file, indent=4)
