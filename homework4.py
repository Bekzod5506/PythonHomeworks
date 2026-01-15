# =========================================
# 1. THEORY QUESTIONS 
# =========================================

# 1. Loops quiz:
#    https://pynative.com/python-if-else-and-for-loop-quiz/
#    

# 2. Difference between break and continue:
#    - break: immediately stops the loop and exits it
#    - continue: skips the current iteration and moves to the next one

# Example:
# for i in range(5):
#     if i == 3:
#         break      # loop stops completely
#     print(i)

# for i in range(5):
#     if i == 3:
#         continue   # skips only this iteration
#     print(i)


# 3. Difference between for loop and while loop:
#    - for loop: used when the number of iterations is known
#    - while loop: used when looping depends on a condition

# Example:
# for i in range(5):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1


# 4. Nested for loop example:
#    A loop inside another loop

# Example:
# for i in range(3):
#     for j in range(2):
#         print(i, j)



# =========================================
# 2. TASK 1: Return uncommon elements of lists


def uncommon_elements(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)

    for item in list2:
        if item not in list1:
            result.append(item)

    return result


# Test cases
print(uncommon_elements([1, 1, 2], [2, 3, 4]))      
print(uncommon_elements([1, 2, 3], [4, 5, 6]))      
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  



# =========================================
# 3. TASK 2: Print square of numbers less than n


n = 5

for i in range(1, n):
    print(i * i)



# =========================================
# 4. TASK 3: Insert underscore after every 3rd character


def insert_underscore(txt):
    result = ""
    count = 0

    for i in range(len(txt)):
        result += txt[i]
        count += 1


        if count == 3 and i != len(txt) - 1 and txt[i] != "_":
            result += "_"
            count = 0

    return result


# Test
print(insert_underscore("hello"))


# Test Task 3
print("Task 3 Tests:")
print(insert_underscore("hello"))        # hel_lo
print(insert_underscore("assalom"))      # ass_alom
print(insert_underscore("abcabcdabcdeabcdefabcdefg"))
print()


# ============================================================
# TASK 4
# Number Guessing Game


import random

def number_guessing_game():
    while True:
        secret = random.randint(1, 100)
        attempts = 10

        print("I have chosen a number between 1 and 100.")

        while attempts > 0:
            guess = int(input("Enter your guess: "))
            attempts -= 1

            if guess > secret:
                print("Too high!")
            elif guess < secret:
                print("Too low!")
            else:
                print("You guessed it right!")
                break

        if guess != secret:
            print("You lost. The number was:", secret)

        again = input("Want to play again? ").lower()
        if again not in ["y", "yes", "ok"]:
            break





# ============================================================
# TASK 5
# Password Checker


def password_checker():
    password = input("Enter password: ")

    if len(password) < 8:
        print("Password is too short.")
        return

    has_upper = False
    for ch in password:
        if ch.isupper():
            has_upper = True
            break

    if not has_upper:
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")



# ============================================================
# TASK 6
# Print all prime numbers between 1 and 100


print("Task 6: Prime Numbers from 1 to 100")
for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
print("\n")


# ============================================================
# BONUS
# Rock, Paper, Scissors Game


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        player = input("Enter rock, paper or scissors: ").lower()
        computer = random.choice(choices)

        print("Computer chose:", computer)

        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("Score -> You:", player_score, " Computer:", computer_score)
        print()

    if player_score == 5:
        print("You won the match!")
    else:
        print("Computer won the match!")



