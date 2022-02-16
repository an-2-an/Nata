from typing import Union
import doctest


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    if len(looking_str) < 2:
        return True
    elif looking_str[0] != looking_str[-1]:
        return False
    else:
        return is_palindrome(looking_str[1:-1])


if __name__ == '__main__':
    doctest.testmod()


