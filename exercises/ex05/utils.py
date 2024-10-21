"""Defining utility funcs"""

__author__ = "730411082"


def only_evens(list1: list[int]) -> list[int]:
    return_list: list[int] = []
    for item in list1:
        if item % 2 == 0:
            return_list.append(item)
    return return_list


def sub(list1: list[int], start: int, end: int) -> list[int]:
    returned_list: list[int] = []
    if start < 0:
        start = 0
    if end > len(list1):
        end = len(list1)
    if len(list1) == 0 or start >= len(list1) or end <= 0:
        return returned_list
    idx: int = start
    while idx < end:
        returned_list.append(list1[idx])
        idx += 1
    return returned_list


def add_at_index(list1: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(list1):
        raise IndexError("Index is out of bounds for the input list")
    if index == len(list1):
        list1.append(element)
    else:
        list1.append(0)
        for idx in range(len(list1) - 1, index, -1):
            list1[idx] = list1[idx - 1]
        list1[index] = element
