__author__ = "730411082"


def find_and_remove_max(list: list[int]) -> int:
    max: int = -1
    for item in list:
        if item > max:
            max = item
    index: int = 0
    while index < len(list):
        if list[index] == max:
            list.pop(index)
        index += 1
    return max
