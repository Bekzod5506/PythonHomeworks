# ===============================
# Task 1: Zero Check Decorator

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# ===============================
# Task 2: Employee Records Manager

import os

EMPLOYEE_FILE = "employees.txt"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    with open(EMPLOYEE_FILE, "a") as f:
        f.write(f"{emp_id},{name},{position},{salary}\n")
    print("Employee added successfully.")

def view_employees():
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return
    with open(EMPLOYEE_FILE, "r") as f:
        records = f.readlines()
    if not records:
        print("No employee records found.")
    else:
        print("Employee Records:")
        for rec in records:
            print(rec.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return
    with open(EMPLOYEE_FILE, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print("Employee Found:", line.strip())
                return
    print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return
    updated = False
    with open(EMPLOYEE_FILE, "r") as f:
        lines = f.readlines()
    with open(EMPLOYEE_FILE, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                print("Current Record:", line.strip())
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                f.write(f"{emp_id},{name},{position},{salary}\n")
                updated = True
            else:
                f.write(line)
    if updated:
        print("Employee updated successfully.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return
    deleted = False
    with open(EMPLOYEE_FILE, "r") as f:
        lines = f.readlines()
    with open(EMPLOYEE_FILE, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                deleted = True
                continue
            f.write(line)
    if deleted:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

def employee_manager():
    while True:
        print("\n--- Employee Records Manager ---")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Try again.")

# ===============================
# Task 3: Word Frequency Counter

import string
from collections import Counter

SAMPLE_FILE = "sample.txt"
REPORT_FILE = "word_count_report.txt"

def create_sample_file():
    text = input("File 'sample.txt' not found. Enter text to create it:\n")
    with open(SAMPLE_FILE, "w") as f:
        f.write(text)

def word_frequency_counter():
    if not os.path.exists(SAMPLE_FILE):
        create_sample_file()
    with open(SAMPLE_FILE, "r") as f:
        text = f.read().lower()  
    
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    total_words = len(words)
    counter = Counter(words)
    
    top_n = input("How many top common words to display? (default 5): ")
    top_n = int(top_n) if top_n.isdigit() else 5
    most_common = counter.most_common(top_n)
    
    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in most_common:
        print(f"{word} - {count} times")
    
    
    with open(REPORT_FILE, "w") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write(f"Top {top_n} Words:\n")
        for word, count in most_common:
            f.write(f"{word} - {count}\n")
    print(f"\nWord count report saved to '{REPORT_FILE}'")

# ===============================
# Main Menu to Run All Tasks

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Division with zero check")
        print("2. Employee Records Manager")
        print("3. Word Frequency Counter")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print("Result:", div(a, b))
        elif choice == "2":
            employee_manager()
        elif choice == "3":
            word_frequency_counter()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
