def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def read_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            limits = ""
            if minimum is not None:
                limits += f" (minimum {minimum}"
                if maximum is not None:
                    limits += f", maximum {maximum}"
                limits += ")"
            print(f"Please enter a valid integer{limits}.")

def read_email(prompt):
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email.split("@")[-1]:
            return email
        print("Please enter a valid email address.")

def print_students(students):
    if not students:
        print("\nNo students found.")
        return

    print("\n" + "-" * 105)
    print(f"{'ID':<12}{'Name':<22}{'Age':<6}{'Course':<22}{'Email':<28}{'Phone':<15}")
    print("-" * 105)
    for s in students:
        print(f"{s.student_id:<12}{s.name:<22}{s.age:<6}{s.course:<22}{s.email:<28}{s.phone:<15}")
    print("-" * 105)
