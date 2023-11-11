import time


def timer(func):
    cache = {}

    def validate_args(*args):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(args[0])

    def memoize(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    def wrapper(*args):
        start_time = time.time()
        result_validated = validate_args(*args)
        end_time = time.time()

        if isinstance(result_validated, str):
            return result_validated

        start_time_memoize = time.time()
        result = memoize(*args)
        end_time_memoize = time.time()

        print(f"Время выполнения функции без memoize: {end_time - start_time} секунд")
        print(f"Время выполнения функции с memoize: {end_time_memoize - start_time_memoize} секунд")
        return result
    return wrapper


@timer
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)
