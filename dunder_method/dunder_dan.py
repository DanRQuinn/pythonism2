# This code defines a class called `Person`.
class Person:

    # The `__init__()` method is called when a new object is created from the `Person` class.
    def __init__(self, name):
        # The `name` attribute stores the name of the person.
        self.name = name

    # The `__dan__()` method is a special method that is called when the object is called like a function.
    # This method adds the prefix "Dan" to the name of the person, unless the name starts with a vowel.
    def __dan__(self):
        # This line defines a list of vowels.
        vowels = ["a", "e", "i", "o", "u"]

        # This line checks if the first character of the name of the person is in the list of vowels.
        if self.name[0] in vowels:
            # This line returns the string "Dan" concatenated with the rest of the name of the person.
            return "Dan" + self.name[1:]
        else:
            # This line returns the string "Dan" concatenated with the first two characters of the name of the person.
            return "Dan" + self.name[1:2] + self.name[2:]

# This line is a special line that is called when the Python interpreter is running the code in the current file.
# This line tells the Python interpreter to execute the code in the indented block if the file is being run as a script.
if __name__ == "__main__":

    # This line creates a new object from the `Person` class.
    # The object is assigned to the variable `p`.
    # The name of the person is "Anthony".
    p = Person("Anthony")

    # This line calls the `__dan__()` method on the object `p`.
    # The result of the `__dan__()` method is printed to the console.
    print(p.__dan__())

    # This line creates a new object from the `Person` class.
    # The object is assigned to the variable `p`.
    # The name of the person is "Logan".
    p = Person("Logan")

    # This line calls the `__dan__()` method on the object `p`.
    # The result of the `__dan__()` method is printed to the console.
    print(p.__dan__())

    # This line creates a new object from the `Person` class.
    # The object is assigned to the variable `p`.
    # The name of the person is "Sarah".
    p = Person("Sarah")

    # This line calls the `__dan__()` method on the object `p`.
    # The result of the `__dan__()` method is printed to the console.
    print(p.__dan__())
