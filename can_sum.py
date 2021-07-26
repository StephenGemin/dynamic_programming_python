"""
The function should return a boolean indicating whether or not it is possible
to generate the target sum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""
import functools
from typing import Iterable, Callable

from core.decorators import memoize, recursive_timer


def _run_recursive(target, num_array, func: Callable):
    if target == 0:
        return True
    if target < 0:
        return False
    for num in num_array:
        if func(target-num, num_array) is True:
            return True
    return False


@recursive_timer
def can_sum(target: int, num_array: Iterable[int]) -> bool:
    return _run_recursive(target, num_array, can_sum)


@recursive_timer
def can_sum_1(target: int, num_array: Iterable[int], memo: dict = {}) -> bool:
    if target in memo:
        return memo[target]
    memo[target] = _run_recursive(target, num_array, can_sum_1)
    return memo[target]


@recursive_timer
@memoize
# @functools.lru_cache
def can_sum_2(target: int, num_array: Iterable[int]) -> bool:
    return _run_recursive(target, num_array, can_sum_2)


if __name__ == '__main__':
    target, numbers, result = 220, (7, 14), False
    assert can_sum(target, numbers) is result
    assert can_sum_1(target, numbers) is result
    assert can_sum_2(target, numbers) is result

    # assert can_sum(7, (2, 3)) is True
    # assert can_sum(7, (5, 3, 4, 7)) is True
    # assert can_sum(7, (2, 4)) is False
    # assert can_sum(8, (2, 3, 5)) is True
    # assert can_sum(220, (7, 14)) is False
