from .models import Student
from .storage import StudentStorage

class StudentManager:
    def __init__(self, storage=None):
        self.storage = storage or StudentStorage()
        self.students = self.storage.load_all()

    def _save(self):
        self.storage.save_all(self.students)

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            raise ValueError("Student ID already exists.")
        if any(s.email.lower() == student.email.lower() for s in self.students):
            raise ValueError("Email already exists.")
        self.students.append(student)
        self._save()

    def get_student(self, student_id):
        return next((s for s in self.students if s.student_id == student_id), None)

    def update_student(self, student_id, **changes):
        student = self.get_student(student_id)
        if not student:
            raise ValueError("Student not found.")

        allowed = {"name", "age", "course", "email", "phone"}
        for field, value in changes.items():
            if field in allowed and value is not None:
                setattr(student, field, value)

        self._save()
        return student

    def delete_student(self, student_id):
        student = self.get_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        self.students.remove(student)
        self._save()

    def search(self, keyword):
        keyword = keyword.lower().strip()
        return [
            s for s in self.students
            if keyword in s.student_id.lower()
            or keyword in s.name.lower()
            or keyword in s.course.lower()
            or keyword in s.email.lower()
            or keyword in s.phone.lower()
        ]

    def filter_by_course(self, course):
        return [s for s in self.students if s.course.lower() == course.lower()]

    def all_students(self):
        return list(self.students)
