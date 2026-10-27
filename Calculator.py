def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(z, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error! Division by zero."
  return x / y

def calculator():
  print("Select operations:")
  print("1. Add (+)")
  print("2. Subtract (-)")
  print("3. Multiply (+)")
  print("4. Divide (/)")

  while True:
    choice = input("\nEnter choice (!/2/3/4) or 'q' to quit: ").strip()
