def length(s: str) -> int:
    """Return the length of the string."""
    raise NotImplementedError

def reverse(s: str) -> str:
    """Return the reversed string."""
    raise NotImplementedError

def starts_with(s: str, prefix: str) -> bool:
    """Return True if s starts with prefix."""
    raise NotImplementedError

def ends_with(s: str, suffix: str) -> bool:
    """Return True if s ends with suffix."""
    raise NotImplementedError

def contains(haystack: str, needle: str) -> bool:
    """Return True if needle occurs within haystack."""
    raise NotImplementedError

def contains_how_often(haystack: str, needle: str) -> int:
    """
    Count overlapping occurrences of needle within haystack.
    Convention: if needle == "", return 0.
    """
    raise NotImplementedError

def first_index_of(haystack: str, needle: str) -> int:
    """
    Return 0-based index of first occurrence of needle; -1 if not found.
    """
    raise NotImplementedError

def last_index_of(haystack: str, needle: str) -> int:
    """
    Return 0-based index of last occurrence of needle; -1 if not found.
    """
    raise NotImplementedError

def index_of_after(haystack: str, needle: str, after_index: int) -> int:
    """
    Return index of first occurrence of needle after after_index; -1 if not found.
    """
    raise NotImplementedError

def sub_string(s: str, start: int, end: int) -> str:
    """
    Return substring s[start:end] (end exclusive).
    """
    raise NotImplementedError

def remove_first(haystack: str, needle: str) -> str:
    """
    Remove the first occurrence of needle from haystack.
    If needle not found, return haystack unchanged.
    """
    raise NotImplementedError

def remove_all(haystack: str, needle: str) -> str:
    """
    Remove all occurrences of needle from haystack.
    """
    raise NotImplementedError

def less(a: str, b: str) -> bool:
    """
    Return True if a is _lexicographically_ smaller than b.
    """
    raise NotImplementedError

def to_roman(n: int) -> str:
    """
    Convert an integer to it's Roman numeral representation (I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000).
    For instance, 2024 is represented as MMXXIV.
    """
    raise NotImplementedError

def replace_first(text: str, old: str, new: str) -> str:
    """
    Replace the first occurrence of 'old' in 'text' with 'new'.
    """
    raise NotImplementedError

def replace_all(text: str, old: str, new: str) -> str:
    """
    Replace all occurrences of 'old' in 'text' with 'new'.
    """
    raise NotImplementedError
