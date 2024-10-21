"""Splitting a dictionary into two lists."""

__author__ = "730411082"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Returns a list of keys in a dictionary."""
    # keys: list[str] = []
    # Autograder check for built-ins
    return list(dictionary.keys())


def get_values(dictionary: dict[str, int]) -> list[int]:
    """returns a list of values in dictionary."""
    # Autograder check for built-ins
    return list(dictionary.values())
