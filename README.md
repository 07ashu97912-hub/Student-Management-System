# Student Management System

A Python console application for managing student records using Object-Oriented Programming, JSON file handling, CRUD operations, searching, filtering, modular design, and exception handling.

## Features

- Add student records
- Update existing student records
- Delete student records
- Search by ID, name, course, email, or phone
- Filter students by course
- View all students
- Persistent storage using JSON
- Input validation and exception handling
- Modular OOP-based architecture
- No external Python packages required

## Project Structure

```text
student-management-system/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── students.json
└── student_management/
    ├── __init__.py
    ├── models.py
    ├── storage.py
    ├── manager.py
    ├── utils.py
    └── cli.py
```

## How to Run

1. Install Python 3.9 or newer.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

## Data Storage

Student records are stored in `data/students.json`. The application automatically creates the file if it does not exist.

## OOP Concepts Used

- `Student` class represents a student entity.
- `StudentStorage` handles persistence.
- `StudentManager` contains business logic and CRUD operations.
- Encapsulation is achieved by separating responsibilities across classes/modules.
- Class methods are used for reconstructing objects from stored JSON data.

## Exception Handling

The system handles invalid input, duplicate student IDs/emails, missing students, malformed JSON data, and file-related errors.

## GitHub Submission

Create a public repository named `student-management-system`, copy the project files into it, then commit and push:

```bash
git init
git add .
git commit -m "Initial Student Management System"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Academic Deliverables

- Public GitHub Repository
- Complete Source Code
- README Documentation
- Project Report PDF

## Future Enhancements

- GUI using Tkinter
- SQLite/MySQL database
- Login and role-based access
- Advanced sorting and pagination
- Export to CSV/PDF
- Unit testing with pytest
