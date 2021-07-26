"""
Say that you are a traveler on a 2D grid.
You begin in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down or right.

In how many ways can you travel to the goal on a grid  dimensions m*n?
"""
import functools

from core.decorators import memoize, recursive_timer


@recursive_timer
def brute_grid_traveler(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    return brute_grid_traveler(m - 1, n) + brute_grid_traveler(m, n - 1)


@recursive_timer
def grid_traveler_1(m: int, n: int, memo: dict = {}) -> int:
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    key = f"{m},{n}"
    if key not in memo:
        memo[key] = grid_traveler_1(m - 1, n, memo) + grid_traveler_1(m, n - 1, memo)
    return memo[key]


@recursive_timer
@memoize
# @functools.lru_cache
def grid_traveler_2(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    return grid_traveler_2(m - 1, n) + grid_traveler_2(m, n - 1)


if __name__ == "__main__":
    m, n = 15, 12
    brute_grid_traveler(m, n)
    grid_traveler_1(m, n)
    grid_traveler_2(m, n)

    # assert brute_grid_traveler(1, 0) == 0
    # assert brute_grid_traveler(0, 1) == 0
    # assert brute_grid_traveler(1, 1) == 1
    # assert brute_grid_traveler(2, 3) == 3
    # assert brute_grid_traveler(3, 2) == 3
    # assert brute_grid_traveler(3, 3) == 6
    # assert brute_grid_traveler(15, 12) == 4457400
