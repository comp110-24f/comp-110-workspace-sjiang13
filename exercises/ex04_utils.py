"""Utils docstring."""

__author__ = "730411082"


def all(list1: list[int], number: int) -> bool:
    for item in list1:
        if item != number:
            return False
    return True


def max(list1: list[int]) -> int:
    if len(list1) == 0:
        raise ValueError("max() arg is an empty list")
    max = 0
    for item in list1:
        if item > max:
            max = item
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for item in list2:
        list1.append(item)
