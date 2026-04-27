"""iteration tools"""
from .compat import builtins, imap


def first(iterable):
    """
    Get the first item in the iterable.
    """
    pass


def last(iterable):
    """
    Get the last item in the iterable.
    Warning, this can be slow due to iter step by step to last one.
    """
    pass


def all(iterable, predicate):
    """
    Returns True if all elements in the given iterable are True for the
    given predicate function.
    """
    pass


def any(iterable, predicate):
    """
    Returns True if any element in the given iterable is True for the
    given predicate function.
    """
    pass


def join(iterable, separator=''):
    """
    Join each item of iterable to string.
    """
    pass
