"""Mutating functions."""

__author__ = "730411082"


def manual_append(list1: list[int], item: int) -> None:
    list1.append(item)
    return None


def double(list1: list[int]) -> None:
    index = 0
    while index < len(list1):
        list1[index] *= 2
        index += 1


list1: list[int] = [1, 2, 3]
list2: list[int] = list1
double(list2)
print(list1)
print(list2)

# should be equal
