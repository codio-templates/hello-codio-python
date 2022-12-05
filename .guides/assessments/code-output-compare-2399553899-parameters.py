import random as r
import math as m

def ellipse_area(a, b):
  return m.pi * a * b

def rectangle_area(w, h):
  return w * h

def triangle_area(w, h):
  return w * h * 0.5

codio_parameters = dict()

choice = r.randint(1, 3)
num1 = r.randint(1, 100)
num2 = r.randint(1, 100)

if choice == 1:
  codio_parameters['shape'] = 'ellipse'
  codio_parameters['func_name'] = 'ellipse_area'
  codio_parameters['num1'] = num1
  codio_parameters['num2'] = num2
  codio_parameters['answer'] = ellipse_area(num1, num2)
  codio_parameters['image'] = 'ellipse.png'
  codio_parameters['description'] = f'a semi-major axis A of {num1} and a semi-major axis B of {num2}'
  codio_parameters['solution_code'] = 'def ellipse_area(a, b):\n\treturn math.pi * a * b'
  codio_parameters['rationale'] = '* Create a function named `ellipse_area` which takes two parameters\n* Return the product of the two parameters and Pi\n* Be sure to use `math.pi` for Pi'
elif choice == 2:
  codio_parameters['shape'] = 'rectangle'
  codio_parameters['func_name'] = 'rectangle_area'
  codio_parameters['num1'] = num1
  codio_parameters['num2'] = num2
  codio_parameters['answer'] = rectangle_area(num1, num2)
  codio_parameters['image'] = 'rectangle.png'
  codio_parameters['description'] = f'a base of {num1} and a height of {num2}'
  codio_parameters['solution_code'] = 'def rectangle_area(b, h):\n\treturn b * h'
  codio_parameters['rationale'] = '* Create a function named `rectangle_area` which takes two parameters\n* Return the product of the two parameters'
else:
  codio_parameters['shape'] = 'triangle'
  codio_parameters['func_name'] = 'triangle_area'
  codio_parameters['num1'] = num1
  codio_parameters['num2'] = num2
  codio_parameters['answer'] = triangle_area(num1, num2)
  codio_parameters['image'] = 'triangle.png'
  codio_parameters['description'] = f'a base of {num1} and a height of {num2}'
  codio_parameters['solution_code'] = 'def triangle_area(b, h):\n\treturn b * h * 0.5'
  codio_parameters['rationale'] = '* Create a function named `triangle_area` which takes two parameters\n* Return half of the product of the two parameters'