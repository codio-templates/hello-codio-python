import sys

# Searching student code for 'while'
with open('iteration_exercise.py') as subfile:
  subtext = subfile.read()
  
  if 'while' not in subtext:
    print("You did not use a while loop!")
    sys.exit(1)
  else:
    print("Well done! You used a while loop!")

sys.exit(0)
