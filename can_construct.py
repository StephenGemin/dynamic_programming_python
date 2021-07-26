"""
Write a function 'can_construct(target, word_bank)' that accepts a target string and
an array of strings

The function should return a boolean indicating whether or not the 'target' can be
constructed by concatenating elements of the 'word_bank' array

You may reuse elements of 'word_bank' as many times as needed
"""
import functools
from typing import Callable, Iterable

from core.decorators import memoize, recursive_timer


def _run_recursive(target, word_bank, func: Callable) -> bool:
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            if func(target[len(word) :], word_bank) is True:
                return True

    return False


@recursive_timer
def can_construct_brute(target: str, word_bank: Iterable[str]):
    return _run_recursive(target, word_bank, can_construct_brute)


@recursive_timer
def can_construct_1(target: str, word_bank: Iterable[str], memo: dict = {}):
    if target in memo:
        return memo[target]
    memo[target] = _run_recursive(target, word_bank, can_construct_1)
    return memo[target]


@recursive_timer
@memoize
@functools.lru_cache
def can_construct_2(target: str, word_bank: Iterable[str]):
    return _run_recursive(target, word_bank, can_construct_2)


if __name__ == "__main__":
    target = "eeeeeeeeeeeeeeeeeeeeeef"
    word_bank = ("e", "ee", "eee", "eeee", "eeeee", "eeeeee")
    result = False
    assert can_construct_brute(target, word_bank) is result
    assert can_construct_1(target, word_bank) is result
    assert can_construct_2(target, word_bank) is result


    # assert can_construct_brute("purple", ["purp", "p", "ur", "le", "purpl"]) is True
    # assert can_construct_brute("purple", ["purp", "z", "ex"]) is False
    # assert (
    #     can_construct_brute("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    #     is False
    # )
    # assert (
    #     can_construct_brute("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
    #     is True
    # )
    # assert can_construct_brute(
    #     "eeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]
    # ) is False
