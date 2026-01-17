# =========================================
# Task 1: Temperature Conversion


def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * 9 / 5 + 32


def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9


# User interaction for Task 1

f = float(input("Enter a temperature in degrees F: "))
c_result = round(convert_far_to_cel(f), 2)
print(f"{f} degrees F = {c_result} degrees C\n")

c = float(input("Enter a temperature in degrees C: "))
f_result = round(convert_cel_to_far(c), 2)
print(f"{c} degrees C = {f_result} degrees F")


# =========================================
# Task 2: Investment Growth


def invest(amount, rate, years):
    """Print investment value for each year"""
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")


# User interaction for Task 2

print("\n--- Investment Calculator ---")
initial_amount = float(input("Enter the initial amount: "))
annual_rate = float(input("Enter the annual rate (e.g. 0.05 for 5%): "))
num_years = int(input("Enter the number of years: "))

invest(initial_amount, annual_rate, num_years)


# =========================================
# Task 3: Factors of a Number


print("\n--- Factor Finder ---")
number = int(input("Enter a positive integer: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")


# =========================================
# Task 4: University Enrollment Statistics


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(data):
    enrollments = []
    tuitions = []
    for uni in data:
        enrollments.append(uni[1])
        tuitions.append(uni[2])
    return enrollments, tuitions


def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)
    mid = len(values) // 2
    if len(values) % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]


students, tuition = enrollment_stats(universities)

print("\n******************************")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}\n")

print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,}")
print("******************************")


# =========================================
# Task 5: Prime Number Checker


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Example usage (optional test)

print("\n--- Prime Number Test ---")
test_num = int(input("Enter a number to check if it is prime: "))
print(is_prime(test_num))
