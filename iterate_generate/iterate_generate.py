def custom_collection(start, end):
  """A custom collection that can be used in a for in loop, list comprehension, and converted to a list."""

  current = start
  while current <= end:
    yield current
    current += 1

def main():
  # Use the custom collection in a for in loop.
  for number in custom_collection(1, 10):
    print(number)

  # Use the custom collection in a list comprehension.
  numbers = [number for number in custom_collection(1, 10)]
  print(numbers)

  # Convert the custom collection to a list.
  list_of_numbers = list(custom_collection(1, 10))
  print(list_of_numbers)

if __name__ == "__main__":
  main()
