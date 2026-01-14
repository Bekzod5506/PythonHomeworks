#number1

num = float(input("Enter a float number: "))
rounded_num = round(num, 2)
print("Rounded number:", rounded_num)

#number2

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = max(a, b, c)
smallest = min(a, b, c)

print("Largest number:", largest)
print("Smallest number:", smallest)

#number3

km = float(input("Enter distance in kilometers: "))

meters = km * 1000
centimeters = km * 100000

print("Meters:", meters)
print("Centimeters:", centimeters)

#number4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

division = a // b
remainder = a % b

print("Integer division result:", division)
print("Remainder:", remainder)

#number5

Celsius = float(input("Enter temperature in Celsius: "))

Fahrenheit = (Celsius * 9/5) + 32
print("Temperature in Fahrenheit:", Fahrenheit)

#number6

num = int(input("Enter a number: "))
last_digit = abs(num) % 10
print("Last digit:", last_digit)

#number7

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#string1

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

print(f"Hello {name}, you are {age} years old.")

#string2

txt = "LMaaslEitbtu"

car1 = txt[::2]   
car2 = txt[1::2] 

print(car1)
print(car2)

#string3

s = input("Enter a string: ")

print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

#string4

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#string5

s = input("Enter a string: ")
vowels = "aeiouAEIOU"

v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)

#string6

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s2 in s1:
    print("Contains")
else:
    print("Does not contain")

#string7

sentence = input("Enter sentence: ")
old = input("Word to replace: ")
new = input("New word: ")

print(sentence.replace(old, new))

#string8

s = input("Enter a string: ")

print("First:", s[0])
print("Last:", s[-1])

#string9

s = input("Enter a string: ")
print(s[::-1])

#string10

s = input("Enter a string: ")
print(s[::-1])

#string11

s = input("Enter a string: ")

if any(ch.isdigit() for ch in s):
    print("Contains digits")
else:
    print("No digits")

#string12

words = ["Python", "is", "fun"]
separator = "-"

result = separator.join(words)
print(result)

#string13

s = input("Enter a string: ")
print(s.replace(" ", ""))

#string14

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Equal")
else:
    print("Not equal")

#string15

sentence = input("Enter a sentence: ")

words = sentence.split()
acronym = ""

for w in words:
    acronym += w[0].upper()

print(acronym)

#string16

s = input("Enter a string: ")
ch = input("Enter character to remove: ")

print(s.replace(ch, ""))

#string17

s = input("Enter a string: ")
vowels = "aeiouAEIOU"

result = ""
for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print(result)

#string18

s = input("Enter a string: ")
start = input("Starts with: ")
end = input("Ends with: ")

if s.startswith(start) and s.endswith(end):
    print("Matches")
else:
    print("Does not match")

#boolean1

username = input("Enter username: ")
password = input("Enter password: ")

if username != "" and password != "":
    print("Both username and password are provided")
else:
    print("One or both fields are empty")

#boolean2

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

#boolean3

n = int(input("Enter a number: "))

if n > 0 and n % 2 == 0:
    print("Positive and even")
else:
    print("Not positive and even")

#boolean4

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a != b and a != c and b != c:
    print("All numbers are different")
else:
    print("Some numbers are the same")

#boolean5

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2):
    print("Same length")
else:
    print("Different length")

#boolean6

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

#boolean7.1

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a + b > 50.8:
    print("Sum is greater than 50.8")
else:
    print("Sum is not greater than 50.8")

#boolean7.2

n = int(input("Enter a number: "))

if 10 <= n <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is outside the range")



