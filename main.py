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

# input defaults to a string
operation = int(input("What operation do you want to perform?\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n"))

if operation == 1:
  print("You picked one.")
elif operation == 2:
  print("You picked two.")

#print(f"What operation do you want to perform?\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")

# in order for your code to repeat you have to have a loop (1. for loops and while loops).
# i suggest that you use a while loop here
