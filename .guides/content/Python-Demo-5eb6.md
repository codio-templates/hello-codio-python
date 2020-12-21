----------

## Iterating Over a List

Python allows you to iterate over a list. That means starting with the first element and progressing through to the end of the list. Using a for loop is the easiest way to iterate over a list.

![Iterating Over a List](.guides/img/iterating-list-variable-name.png)

<details><summary><b>Number and Numbers</b></summary>In the example below, the iteration variable is <code>number</code> and the list is named <code>numbers</code>. This is a very common practice in Python. The list is always plural, while the iterating variable is the singular of the list name. Python will not throw an error if this convention is not followed. However, <code>for number in numbers</code> helps with the readability of your code. You should follow this convention as often as possible.</details>

```python
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
```

[Code Visualizer](open_tutor python_demo.py)
{try it}(python3 python_demo.py 1)

|||challenge
## What happens if you:
* Change the [print statement](open_file python_demo.py panel=0 ref="print" count=1) to `print(numbers)`?

[Remove highlighting](open_file python_demo.py panel=0)

|||

[Code Visualizer](open_tutor python_demo.py)
{try it}(python3 python_demo.py 2)

{Check It!|assessment}(parsons-puzzle-2650837085)
