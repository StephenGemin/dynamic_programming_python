"""
Write a function 'all_construct(target, word_bank)' that accepts a target string and an
array of strings

The function should return a 2D array containing all of the ways that the 'target' can
be constructed by concatenating elements of the 'word_bank' array.  Each element of the
2D array should represent one combination that constructs the 'target'.

You may reuse elements of 'word_bank' as many times as needed
"""
import functools
from typing import Iterable, Callable, List

from core.decorators import memoize, recursive_timer


def _run_recursive(target, word_bank, func: Callable) -> List[List[str]]:
    if target == "":
        return [[]]

    output = []

    for word in word_bank:
        if target.find(word) == 0:
            new_target = target.lstrip(word)
            suffix_ways = func(new_target, word_bank)
            branch_way = [[word] + way for way in suffix_ways]
            if branch_way:
                output.extend(branch_way)
    return output


@recursive_timer
def all_construct(target: str, word_bank: Iterable[str]):
    return _run_recursive(target, word_bank, all_construct)


@recursive_timer
@memoize
# @functools.lru_cache
def all_construct_1(target: str, word_bank: Iterable[str]):
    return _run_recursive(target, word_bank, all_construct_1)


if __name__ == "__main__":
    """
    Note for this example, there is only a special use case where memoizing is useful.
    """
    _target = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    _word_bank = ("e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee", "eeeeeee",
                  "eeeeeeee", "eeeeeeeee", "f", "ff",)
    _result = [["e", "f"], ["ee", "f"], ["eee", "f"], ["eeee", "f"], ["eeeee", "f"],
               ["eeeeee", "f"], ["eeeeee", "f"], ["eeeeeee", "f"], ["eeeeeeee", "f"],
               ["eeeeeeeee", "f"], ]
    assert all_construct(_target, _word_bank) == _result
    assert all_construct_1(_target, _word_bank) == _result

    # result = [["purp", "le"], ["p", "ur", "p", "le"]]
    # assert all_construct("purple", ("purp", "p", "ur", "le", "purpl")) == result
    #
    # result = [["ab", "cd", "ef"], ["ab", "c", "def"], ["abc", "def"], ["abcd", "ef"]]
    # assert (
    #     all_construct("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef", "c")) == result
    # )
    #
    # assert all_construct(_target, _word_bank) == _result
