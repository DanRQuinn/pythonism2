# pythonism2

## Creator

Dan Quinn, Logan Reese, Sarah Glass, and Anthony Sinitsa

## Project Description

This repository contains three Python files:

* `logging_decorator.py`
* `person.py`
* `custom_collection.py`

## logging_decorator.py

This file defines a decorator called `logging_decorator`. The `logging_decorator` decorator can be used to wrap any function. When the wrapped function is called, the `logging_decorator` decorator will print the name of the function and its arguments to the console. The `logging_decorator` decorator will also print the return value of the wrapped function to the console.

```python
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function {} with arguments {}".format(func.__name__, args))
        result = func(*args, **kwargs)
        print("Function {} returned {}".format(func.__name__, result))
        return result
    return wrapper


## person.py

This file defines a class called `Person`. The `Person` class has two attributes:

* `name`: The name of the person.
* `dan`: A method that returns the name of the person with the prefix "Dan" added to it, unless the name starts with a vowel.

python
class Person:

    def __init__(self, name):
        self.name = name

    def __dan__(self):
        vowels = ["a", "e", "i", "o", "u"]
        if self.name[0] in vowels:
            return "Dan" + self.name[1:]
        else:
            return "Dan" + self.name[1:2] + self.name[2:]


## custom_collection.py

This file defines a function called `custom_collection`. The `custom_collection` function returns a custom collection that can be used in a for in loop, list comprehension, and converted to a list. The `custom_collection` function takes two arguments:

* `start`: The starting number of the collection.
* `end`: The ending number of the collection.

python
def custom_collection(start, end):
    """A custom collection that can be used in a for in loop, list comprehension, and converted to a list."""

    current = start
    while current <= end:
        yield current
        current += 1


## Usage

To use the code in this repository, you can clone the repository to your local machine and then import the modules into your Python code.

For example, to use the `logging_decorator` decorator, you can import the `logging_decorator` module and then use the `logging_decorator` decorator to wrap any function.

python
from logging_decorator import logging_decorator

@logging_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# pythonism2
