"""
Write a function 'fib(n)' that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.

The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.
"""
import functools

from core.decorators import memoize, recursive_timer


@recursive_timer
def brute_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return brute_fibonacci(n - 2) + brute_fibonacci(n - 1)


@recursive_timer
def fibonacci_1(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_1(n - 2) + fibonacci_1(n - 1)
    return memo[n]


@recursive_timer(stdout=False)
@memoize
# @functools.lru_cache
def fibonacci_2(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_2(n - 2) + fibonacci_2(n - 1)


if __name__ == "__main__":
    # assert brute_fibonacci(6) == 8
    # assert brute_fibonacci(7) == 13
    # assert brute_fibonacci(8) == 21
    # assert brute_fibonacci(33) == 3524578

    _n = 33
    # brute_fibonacci(_n)
    # fibonacci_1(_n)
    fibonacci_2(_n)
