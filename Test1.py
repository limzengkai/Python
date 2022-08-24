def add(numbers):
    """
    >>> add([])
    0
    >>> add([25])
    0
    >>> add([92, 61, 97, 10, -39])
    71
    >>> add([-24, -25, -33, 32, -81, -58, 28, -4, -30, -69, 44, -41])
    -165
    """
    index = 0
    sum_var = 0
    while index < len(numbers):
        if index%2!=0:
            sum_var += numbers[index]
        index += 1
    return sum_var

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
