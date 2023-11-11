def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper


@validate_args
def example_function(num):
    return num


print(example_function(5))
print(example_function())
print(example_function(5, 6))
print(example_function("hello"))
print(example_function(-3))
