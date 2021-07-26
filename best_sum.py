"""
Write a function 'best_sum(target_sum, numbers)' that takes in a target sum and an
array of numbers as arguments.

The function should return an array containing the shortest combination of numbers that
add up to exactly the target sum.

If there is a tie for the shortest combination, you may return any one of the shortest.
"""
import functools
from typing import Optional, List, Iterable, Callable

from core.decorators import memoize, recursive_timer


def _run_recursive(target_sum, numbers, func: Callable):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    shortest_combination = None

    for num in numbers:
        branch_result = func(target_sum - num, numbers)
        if branch_result is None:
            continue  # on to next number

        branch_result = [num] + branch_result
        if shortest_combination is None or len(branch_result) < len(
            shortest_combination
        ):
            shortest_combination = branch_result
    return shortest_combination


@recursive_timer
def best_sum_brute(target_sum: int, numbers: Iterable[int]) -> Optional[List[int]]:
    return _run_recursive(target_sum, numbers, best_sum_brute)


@recursive_timer
def best_sum_1(
    target_sum: int, numbers: Iterable[int], memo: dict = {}
) -> Optional[List[int]]:
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None
    shortest_combination = None

    for num in numbers:
        branch_result = best_sum_1(target_sum - num, numbers)
        if branch_result is None:
            memo[target_sum] = branch_result
            continue  # on to next number

        memo[target_sum] = [num] + branch_result
        if shortest_combination is None or len(memo[target_sum]) < len(
            shortest_combination
        ):
            shortest_combination = memo[target_sum]
    return shortest_combination


@recursive_timer
@memoize
# @functools.lru_cache
def best_sum_2(target_sum: int, numbers: Iterable[int]) -> Optional[List[int]]:
    return _run_recursive(target_sum, numbers, best_sum_2)


if __name__ == "__main__":
    target_sum, numbers, result = 26, (1, 2, 5, 13), [13, 13]
    assert best_sum_brute(target_sum, numbers) == result
    assert best_sum_1(target_sum, numbers) == result
    assert best_sum_2(target_sum, numbers) == result
    #
    # assert best_sum_brute(7, (5, 3, 4, 7)) == [7]
    # assert best_sum_brute(8, (2, 3, 5)) == [3, 5]
    # assert best_sum_brute(8, (1, 4, 5)) == [4, 4]
    # assert best_sum_brute(28, (1, 2, 5, 14)) == [14, 14]
