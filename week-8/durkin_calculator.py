# Author: Evan Durkin
# Title: Exercise 8.3
# Date: 12/12/2021

# assigns first and last name and prints string
first_name = "Evan"
last_name = "Durkin"
print(first_name + '' + last_name)

# assigns even and odd numbers
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
# assigns numbers to individual variables
number01 = 4
number02 = 7
number03 = 1
number04 = 8
number05 = 2

# statement to evaluate number and print string
if number01 in even_numbers:
    print(str(number01) + " is an even number")
else:
    print(str(number01) + " is an odd number")

if number02 in odd_numbers:
    print(str(number02) + " is an odd number")
else:
    print(str(number02) + " is an even number")


def hello_world():
    return "Hello World"


print(hello_world())


def my_world(name):
    return "You are now in {} world".format(name)


print(my_world("Durkin's"))

# functions for adding, subtracting and dividing


def add(number01, number02):
    return number01 + number02


def subtract(number01, number03):
    return number01 - number03


def divide(number04, number05):
    return number04 / number05


# prints formula functions
print(add(number01, number02))
print(subtract(number01, number03))
print(divide(number04, number05))
