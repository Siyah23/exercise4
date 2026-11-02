# question 1
fruits = ["apple", "banana", "orange", "pear"]
for fruit in fruits:
  print(fruit)

# question 2
count = 5
while count >= 1:
  print(count)
  count -= 1

# question 3
for number in range(1, 11):
  print(number ** 2)

# question 4
import random
colors = ["red", "blue", "yellow", "purple", "green"]
for int in range(3):
  print(random. choice(colors))

# question 5
import math_operations                     
print(math_operations . add(6, 4))
print(math_operations. subtract(6, 4))
print(math_operations. multiply(6, 4))
print(math_operations. divide(6, 4))

while True:
  first_number = float(input("enter the first number: "))
  operator = (input("enter an operation(+, -, *, / ) or q to quit: "))
  if operator. lower() == "q": break
  second_number = float(input("enter the second number: "))
  if operator == "+":
    print(math_operations. add(first_number, second_number))
  elif operator == "-":
    print(math_operations. subtract(first_number, second_number))
  elif operator == "*":
    print(math_operations. multiply(first_number, second_number))
  elif operator == "/":
    print(math_operations. divide(first_number, second_number))
  else:
    print("invalid_operation")