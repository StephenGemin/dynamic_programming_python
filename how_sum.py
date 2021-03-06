"""
Write a function 'how_sum(target_sum, numbers)' that takes in a target sum and an
array of numbers as arguments.

The function should return an array containing any combination of elements that add up
to exactly the target sum. If there is no combination that adds up to the target sum,
then return None
"""
import functools
from typing import Optional, List, Iterable, Callable

from core.decorators import memoize, recursive_timer


def _run_recursive(target_sum, numbers, func: Callable):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        branch_result = func(remainder, numbers)
        if branch_result is not None:
            return branch_result + [num]
    return None


@recursive_timer
def how_sum_brute(target_sum: int, numbers: Iterable[int]) -> Optional[List[int]]:
    return _run_recursive(target_sum, numbers, how_sum_brute)


@recursive_timer
def how_sum_1(
    target_sum: int, numbers: Iterable[int], memo: dict = {}
) -> Optional[List[int]]:
    if target_sum in memo:
        return memo[target_sum]
    memo[target_sum] = _run_recursive(target_sum, numbers, how_sum_1)
    return memo[target_sum]


@recursive_timer
@memoize
# @functools.lru_cache
def how_sum_2(target_sum: int, numbers: Iterable[int]) -> Optional[List[int]]:
    return _run_recursive(target_sum, numbers, how_sum_2)


if __name__ == "__main__":
    target_sum, numbers = 220, (7, 14)
    assert how_sum_brute(target_sum, numbers) is None
    assert how_sum_1(target_sum, numbers) is None
    assert how_sum_2(target_sum, numbers) is None

    # assert how_sum_brute(7, (2, 3)) == [3, 2, 2]
    # assert how_sum_brute(7, (5, 3, 4, 7)) == [4, 3]
    # assert how_sum_brute(7, (2, 4)) is None
    # assert how_sum_brute(8, (2, 3, 5)) == [2, 2, 2, 2]
    # assert how_sum_brute(220, (7, 14)) is None
