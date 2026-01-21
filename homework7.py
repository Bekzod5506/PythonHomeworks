"""
===========================================================
1. Generalized Vector Class
2. Employee Records Manager (OOP + File Handling)
3. To-Do Application with Multiple File Format Support

"""

import math
import json
import csv
import os
from abc import ABC, abstractmethod

# ===========================================================
# 1. GENERALIZED VECTOR CLASS


class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        # Dot product
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        # Scalar multiplication
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operand")

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[x / mag for x in self.components])

    def __str__(self):
        return f"Vector{self.components}"


# ===========================================================
# 2. EMPLOYEE RECORDS MANAGER
# ===========================================================

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_list(self):
        return [self.employee_id, self.name, self.position, self.salary]


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, "w").close()

    def _read_all(self):
        employees = []
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                emp_id, name, position, salary = line.strip().split(", ")
                employees.append(Employee(emp_id, name, position, float(salary)))
        return employees

    def _write_all(self, employees):
        with open(self.FILE_NAME, "w") as file:
            for emp in employees:
                file.write(str(emp) + "\n")

    def add_employee(self, employee):
        employees = self._read_all()
        if any(emp.employee_id == employee.employee_id for emp in employees):
            print("Employee ID already exists.")
            return
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self, sort_by=None):
        employees = self._read_all()
        if sort_by == "salary":
            employees.sort(key=lambda e: e.salary)
        elif sort_by == "name":
            employees.sort(key=lambda e: e.name)

        for emp in employees:
            print(emp)

    def search_employee(self, employee_id):
        for emp in self._read_all():
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(emp)
                return
        print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employees = self._read_all()
        for emp in employees:
            if emp.employee_id == employee_id:
                if name:
                    emp.name = name
                if position:
                    emp.position = position
                if salary:
                    emp.salary = salary
                self._write_all(employees)
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self, employee_id):
        employees = self._read_all()
        updated = [emp for emp in employees if emp.employee_id != employee_id]
        if len(updated) == len(employees):
            print("Employee not found.")
            return
        self._write_all(updated)
        print("Employee deleted successfully!")


# ===========================================================
# 3. TO-DO APPLICATION WITH MULTIPLE FILE FORMATS


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


# ---------- Storage Interface ----------
class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass


# ---------- JSON Storage ----------
class JSONStorage(StorageStrategy):
    FILE = "tasks.json"

    def save(self, tasks):
        with open(self.FILE, "w") as file:
            json.dump([t.to_dict() for t in tasks], file, indent=4)

    def load(self):
        if not os.path.exists(self.FILE):
            return []
        with open(self.FILE, "r") as file:
            data = json.load(file)
            return [Task.from_dict(d) for d in data]



class CSVStorage(StorageStrategy):
    FILE = "tasks.csv"

    def save(self, tasks):
        with open(self.FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["task_id", "title", "description", "due_date", "status"])
            for t in tasks:
                writer.writerow([t.task_id, t.title, t.description, t.due_date, t.status])

    def load(self):
        if not os.path.exists(self.FILE):
            return []
        tasks = []
        with open(self.FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task(**row))
        return tasks



class TodoManager:
    def __init__(self, storage: StorageStrategy):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("Task ID already exists.")
            return
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    if value:
                        setattr(task, key, value)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        for task in self.tasks:
            if task.status.lower() == status.lower():
                print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully!")


"""
===========================================================
BONUS DESIGN EXPLANATION (SHORT)


Minimal code changes for new file formats were achieved by:
- Using the Strategy Pattern (StorageStrategy)
- The TodoManager depends on an abstract interface
- Adding a new format only requires creating a new storage class
  without modifying existing logic
"""
