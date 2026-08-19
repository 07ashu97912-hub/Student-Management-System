from .models import Student
from .manager import StudentManager
from .utils import read_non_empty, read_int, read_email, print_students

def add_student(manager):
    print("\n--- Add Student ---")
    student = Student(
        student_id=read_non_empty("Student ID: "),
        name=read_non_empty("Name: "),
        age=read_int("Age: ", 1, 120),
        course=read_non_empty("Course: "),
        email=read_email("Email: "),
        phone=read_non_empty("Phone: ")
    )
    manager.add_student(student)
    print("Student added successfully.")

def update_student(manager):
    print("\n--- Update Student ---")
    student_id = read_non_empty("Student ID to update: ")
    student = manager.get_student(student_id)
    if not student:
        raise ValueError("Student not found.")

    print("Press Enter to keep the current value.")
    name = input(f"Name [{student.name}]: ").strip() or None
    age_text = input(f"Age [{student.age}]: ").strip()
    age = int(age_text) if age_text else None
    course = input(f"Course [{student.course}]: ").strip() or None
    email = input(f"Email [{student.email}]: ").strip() or None
    phone = input(f"Phone [{student.phone}]: ").strip() or None

    manager.update_student(student_id, name=name, age=age, course=course,
                           email=email, phone=phone)
    print("Student updated successfully.")

def delete_student(manager):
    print("\n--- Delete Student ---")
    student_id = read_non_empty("Student ID to delete: ")
    manager.delete_student(student_id)
    print("Student deleted successfully.")

def search_student(manager):
    keyword = read_non_empty("Search keyword: ")
    print_students(manager.search(keyword))

def filter_students(manager):
    course = read_non_empty("Course to filter by: ")
    print_students(manager.filter_by_course(course))

def main():
    manager = StudentManager()

    actions = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": search_student,
        "5": lambda m: print_students(m.all_students()),
        "6": filter_students,
    }

    while True:
        print("""
========================================
      STUDENT MANAGEMENT SYSTEM
========================================
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. View All Students
6. Filter by Course
7. Exit
========================================""")
        choice = input("Enter choice: ").strip()

        if choice == "7":
            print("Thank you for using the Student Management System.")
            break

        action = actions.get(choice)
        if not action:
            print("Invalid choice. Please select 1-7.")
            continue

        try:
            action(manager)
        except (ValueError, TypeError) as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")

if __name__ == "__main__":
    main()
