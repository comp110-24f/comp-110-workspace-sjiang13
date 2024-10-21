__author__ = "730411082"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    a: list[int] = [20, 21, 23, 19, 24]
    assert find_and_remove_max(a) == 24


def test_find_and_remove_max_mutate() -> None:
    a: list[int] = [4, 1, 2, 4]
    find_and_remove_max(a)
    assert len(a) == 2


def test_find_and_remove_max_edge() -> None:
    a: list[int] = []
    assert find_and_remove_max(a) == -1
