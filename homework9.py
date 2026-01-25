# =========================
# TASK 1: LIBRARY MANAGEMENT SYSTEM

# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < Member.MAX_BOOKS


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.title] = book

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in the library.")

        book = self.books[book_title]
        member = self.members[member_name]

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed.")

        if not member.can_borrow():
            raise MemberLimitExceededException("Member borrowing limit exceeded.")

        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        member = self.members[member_name]
        book = self.books.get(book_title)

        if book and book in member.borrowed_books:
            book.is_borrowed = False
            member.borrowed_books.remove(book)


# ---- Testing Task 1 

print("=== TASK 1: LIBRARY MANAGEMENT SYSTEM ===")

library = Library()

library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Python Basics", "John Smith"))
library.add_book(Book("Data Science", "Jane Doe"))

library.add_member(Member("Alice"))
library.add_member(Member("Bob"))

try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "Python Basics")
    library.borrow_book("Alice", "Data Science")
    library.borrow_book("Alice", "Nonexistent Book")
except Exception as e:
    print("Error:", e)

library.return_book("Alice", "1984")
print("Alice borrowed books:", library.members["Alice"].borrowed_books)

print()


# =========================
# TASK 2: STUDENT GRADES MANAGEMENT (CSV)


import csv

print("=== TASK 2: STUDENT GRADES MANAGEMENT ===")

# Create grades.csv
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Grade"])
    writer.writerow(["Alice", "Math", 85])
    writer.writerow(["Bob", "Science", 78])
    writer.writerow(["Carol", "Math", 92])
    writer.writerow(["Dave", "History", 74])

grades = []

# Read grades.csv

with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])
        grades.append(row)

# Calculate averages

subject_totals = {}
subject_counts = {}

for entry in grades:
    subject = entry["Subject"]
    grade = entry["Grade"]

    subject_totals[subject] = subject_totals.get(subject, 0) + grade
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

# Write average_grades.csv

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject in subject_totals:
        avg = subject_totals[subject] / subject_counts[subject]
        writer.writerow([subject, avg])

print("average_grades.csv created successfully")
print()


# =========================
# TASK 3: JSON HANDLING


import json

print("=== TASK 3: JSON HANDLING ===")

tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

# Create tasks.json
with open("tasks.json", "w") as file:
    json.dump(tasks_data, file, indent=4)

# Load tasks.json
with open("tasks.json", "r") as file:
    tasks = json.load(file)

# Display tasks
for task in tasks:
    print(
        f"ID: {task['id']}, "
        f"Task: {task['task']}, "
        f"Completed: {task['completed']}, "
        f"Priority: {task['priority']}"
    )

# Task statistics
def task_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total if total > 0 else 0

    return total, completed, pending, avg_priority


total, completed, pending, avg_priority = task_statistics(tasks)

print("\nTask Statistics:")
print("Total tasks:", total)
print("Completed tasks:", completed)
print("Pending tasks:", pending)
print("Average priority:", avg_priority)

# Save changes back to JSON (example: mark task 1 completed)

tasks[0]["completed"] = True

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

# Convert JSON to CSV

with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task", "Completed", "Priority"])
    for task in tasks:
        writer.writerow([
            task["id"],
            task["task"],
            task["completed"],
            task["priority"]
        ])

print("\ntasks.csv created successfully")
