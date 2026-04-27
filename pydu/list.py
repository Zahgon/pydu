
try:
    # Python 3
    from collections.abc import Iterable
except ImportError:
    # Python 2.7
    from collections import Iterable

from pydu.compat import strbytes_types


def uniq(seq, key=None):
    """
    Removes duplicate elements from a list while preserving the order of the rest.

    The value of the optional `key` parameter should be a function that
    takes a single argument and returns a key to test the uniqueness.
    """
    pass


def tolist(obj):
    """
    Convert given `obj` to list.

    If `obj` is not a list, return `[obj]`, else return `obj` itself.
    """
    pass


# https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
def flatten(seq):
    """
    Generate each element of the given `seq`. If the element is iterable and
    is not string, it yields each sub-element of the element recursively.
    """
    pass
