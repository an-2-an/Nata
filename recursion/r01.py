from typing import Union
import doctest


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """
    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    Traceback (most recent call last):
    ...
    ValueError: This function works only with exp > 0.
    """
    if exp < 0:
        raise ValueError('This function works only with exp > 0.')
    if exp == 0:
        return 1
    return to_power(x=x, exp=exp-1) * x


if __name__ == '__main__':
    doctest.testmod()


