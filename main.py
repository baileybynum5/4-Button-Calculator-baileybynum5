def add(x, y):
  answer = x + y
  return answer

def subtract(x, y):
  answer = x - y
  return answer

def multiply(x, y):
  answer = x * y
  return answer

def divide(x, y):
  answer = x / y
  return answer

# create some initial condition for the "some condition"

r = "yes"

while r == "yes":
  # input defaults to a string
  operation = int(input("What operation do you want to perform?\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n"))

  if operation == 1:
    print("You picked 1.")
  elif operation == 2:
    print("You picked 2.")
  elif operation == 3:
    print("You picked 3.")
  elif operation == 4:
    print("You picked 4.")

# you ask a question that changes the value of the condition in row 17 ?

# in order for your code to repeat you have to have a loop (1. for loops and while loops).
# i suggest that you use a while loop here
