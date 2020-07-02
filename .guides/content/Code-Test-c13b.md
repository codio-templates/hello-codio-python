----------

## Standard Code Test

Write a program that takes an integer from the user. Return the number multiplied by three. If the user enters a non-integer data type, return the following message:

`Please enter an integer`

**Note**, it is important that there is no string prompting the user to input a number. The string will cause the code test to fail.

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
