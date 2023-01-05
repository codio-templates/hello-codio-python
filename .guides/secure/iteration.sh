#!/bin/sh

OUTPUT1=$(python3 iteration_exercise.py)   #This calls the student code file iteration_exercise.py

#Checks the code file for errors
if [ $? -ne 0 ]; then   
  echo "</br><hr/><h3>Your code has errors!</h3>"
  echo "Try correcting the errors listed above."
  exit 1
fi

#Checks the output 
#If no output:
if [ -z "$OUTPUT1" ]; then    
  echo "<br/><hr/><h3>Challenge Feedback</h3>"
  echo "Your code does not seem to be outputting anything. Make sure you include a print statement."
  exit 1
#If output does not match:
elif [ "$OUTPUT1" != "7
14
21
28
35
42
49" ]; then 
  echo "<br/><hr/><h3>Challenge Feedback</h3>"
  echo "Your code is not outputting the correct result. It is outputting:"
  echo "$OUTPUT1"
  exit 1
fi

#Calls .guides/secure/iteration_check.py to examine while loop
python3 .guides/secure/iteration_check.py
if [ $? -ne 0 ]; then 
  echo "</br><hr/><h3>Something is not quite right...</h3>"
  echo "Your output is correct but see the comments above to ensure you are following the assignment guidelines."
  exit 1
fi

#Message if no errors found, code is correct and used while loop
echo "<h3>Your code is error-free and works as expected!</h3>"
echo "Nice work."
exit 0