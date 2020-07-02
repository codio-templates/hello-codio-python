num = input("Enter an integer: ")
try:
  num = int(num)
  print(num * 3)
except ValueError:
  print("Please enter an integer")