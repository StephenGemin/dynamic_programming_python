"""
Write a function 'fib(n)' that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.

The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.
"""
import functools
from typing import Callable

from core.decorators import memoize, recursive_timer


def _run_recursive(n, func: Callable):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return func(n - 2) + func(n - 1)


@recursive_timer
def brute_fibonacci(n: int) -> int:
    return _run_recursive(n, brute_fibonacci)


@recursive_timer
def fibonacci_1(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    memo[n] = _run_recursive(n, fibonacci_1)
    return memo[n]


@recursive_timer
@memoize
# @functools.lru_cache
def fibonacci_2(n: int) -> int:
    return _run_recursive(n, fibonacci_2)


if __name__ == "__main__":
    # assert brute_fibonacci(6) == 8
    # assert brute_fibonacci(7) == 13
    # assert brute_fibonacci(8) == 21
    # assert brute_fibonacci(33) == 3524578

    _n = 33
    brute_fibonacci(_n)
    fibonacci_1(_n)
    fibonacci_2(_n)
