def fibonacci(result):
    if result < 2:
        return result
    else:
        return fibonacci(result - 1) + fibonacci(result - 2)

print(fibonacci(int(input())))