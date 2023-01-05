----------

Here's an example of an **Advanced Code Test** in action. Just as before, the **TRY IT** button will test your code and the **Check It!** button will submit your code for grading.

<table><tbody ><tr><td><details><summary>
	<strong>What exactly is being tested</strong>
</summary>

This Advanced Code Test checks the student code file by calling a bash file located in the /.guides/secure folder (which students cannot access) and does the following:
 1. Checks that the code is error free
 2. Checks if something is printed to the console
 3. Compares output to expected result
 4. Calls .guides/secure/iteration_check.py to ensure a `while` loop is used

Each check above echoes a specific message to the student (if it fails) and it will be marked incorrect.

Here's a link to more info on [creating your own Advanced Code Test](https://docs.codio.com/instructors/authoring/assessments/advanced-code-test.html#:~:text=The%20advanced%20code%20test%20assessment,executables%2C%20place%20them%20in%20the%20.).

</details></td></tr></tbody>
</table>


## Advanced Code Test Example

**Instructions:** Use a `while` loop to print the multiples of 7 between 0 and 50.
- Each number should be printed on its own line
- Your code *must* iterate over a `while` loop: using a `for` loop will result in an incorrect response.

Test your code using the button
{Try it}(python3 iteration_exercise.py)
##

<details>

<summary><strong>Possible Solution 1:</strong></summary>

```
count = 7
while count < 50:
  print(count)
  count +=7
```

</details>

## 

<details>

<summary><strong>Possible Solution 2:</strong></summary>

```
count = 1
while count < 8:
  print(count*7)
  count +=1
```

</details>

## 

<details>

<summary><strong>What happens if a for loop is used?</strong></summary>

```
for i in range(7, 50, 7):
  print(i)
```

</details>

## 

{Check It!|assessment}(test-1360603613)