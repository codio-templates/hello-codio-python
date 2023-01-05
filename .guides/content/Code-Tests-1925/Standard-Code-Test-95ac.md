----------

The question below shows Codio's **Standard Code Test** in action. You can enter your code in the file window shown on the left (feel free to copy and paste the correct code under the *Solution* dropdown menu below) 
 - Test your code with the **TRY IT** button (it will run your file in the terminal)
 - Submit your code for grading using the **Check It!** button

<table><tbody ><tr><td><details><summary>
	<strong>What exactly is being tested</strong>
</summary>

The Standard Code Test allows you to generate expected output values based on particular inputs. The test will then run the student's code file with the specified inputs and check them against the expected outputs.

These are the input values being tested with their expected outputs for this example:

| INPUT - STDIN | Expected Output         |
| ------------- | ----------------------- |
| 3             | 9                       |
| -5            | -15                     |
| abc           | Please enter an integer |	

Here's a link to more info on [creating your own Standard Code Test](https://docs.codio.com/instructors/authoring/assessments/standard-code-test.html#:~:text=Standard%20code%20tests%20are%20dialog,the%20student%20code's%20actual%20output.).

</details></td></tr></tbody>
</table>


## Standard Code Test Example

Write a program that takes an integer from the user. Return the number multiplied by three. If the user enters a non-integer data type, return the following message:

`Please enter an integer`

**Note**, it is important that if there is a string prompting the user to input a number, then the standard code test should search for a substring match.

[Code Visualizer](open_tutor code/code_test.py)
{try it|terminal}(python3 code/code_test.py)

<table><tbody ><tr><td><details><summary>
	<strong>Solution</strong>
</summary>

Here is one solution to the problem. You can copy/paste it into the IDE if you would like.

```python
num = input("Enter an integer: ")
try:
  num = int(num)
  print(num * 3)
except ValueError:
  print("Please enter an integer")
```

The `try... except` block catches all non-integers passed to the script.
	
</details></td></tr></tbody>
</table>

{Check It!|assessment}(code-output-compare-2673740583)
