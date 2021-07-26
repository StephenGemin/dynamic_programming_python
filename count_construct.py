"""
Write a function 'can_construct(target, word_bank)' that accepts a target string and
an array of strings

The function should return the number of ways that the 'target' can be
constructed by concatenating elements of the 'word_bank' array

You may reuse elements of 'word_bank' as many times as needed
"""
import functools
from typing import Iterable, Callable

from core.decorators import memoize, recursive_timer


def _run_recursive(target, word_bank, func: Callable) -> int:
    if target == "":
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            num_ways_remaining = func(target[len(word) :], word_bank)
            count += num_ways_remaining
    return count


@recursive_timer
def count_construct(target: str, word_bank: Iterable[str]):
    return _run_recursive(target, word_bank, count_construct)


@recursive_timer
def count_construct_1(target: str, word_bank: Iterable[str], memo: dict = {}):
    if target in memo:
        return memo[target]
    memo[target] = _run_recursive(target, word_bank, count_construct_1)
    return memo[target]


@recursive_timer
@memoize
# @functools.lru_cache
def count_construct_2(target: str, word_bank: Iterable[str]):
    return _run_recursive(target, word_bank, count_construct_2)


if __name__ == "__main__":
    target = "eeeeeeeeeeeeeeeeeeeeeeef"
    word_bank = ("e", "ee", "eee", "eeee", "eeeee", "eeeeee")
    result = 0
    assert count_construct(target, word_bank) == result
    assert count_construct_1(target, word_bank) == result
    assert count_construct_2(target, word_bank) == result

    # assert count_construct("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
    # assert count_construct("purple", ["purp", "z", "ex"]) == 0
    # assert (
    #     count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    #     == 0
    # )
    # assert count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == 4
    # assert (
    #     count_construct(
    #         target, word_bank
    #     )
    #     == 0
    # )
