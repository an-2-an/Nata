import doctest


def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    Traceback (most recent call last):
    ...
    ValueError: input string must be digit string
    """
    if not digit_string:
        return 0

    if not digit_string.isdecimal():
        raise ValueError("input string must be digit string")

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


if __name__ == '__main__':
    doctest.testmod()
