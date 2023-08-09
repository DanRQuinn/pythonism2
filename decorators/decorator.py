def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function {} with arguments {}".format(func.__name__, args))
        result = func(*args, **kwargs)
        print("Function {} returned {}".format(func.__name__, result))
        return result
    return wrapper

@logging_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
