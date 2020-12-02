def my_function(*args, **kwargs):
    s = 0
    if len(args) == 0:
        return 0
    for i in args:
        if type(i) == int or type(i) == float:
            s += i
    return s


def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


def sum_even_numbers(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even_numbers(n - 1)
    else:
        return sum_even_numbers(n - 1)


def sum_odd_numbers(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + sum_odd_numbers(n - 1)
    else:
        return sum_odd_numbers(n - 1)


def read():
    x = input("Enter a number:\n")
    try:
        number = int(x)
        return number
    except ValueError:
        return 0
