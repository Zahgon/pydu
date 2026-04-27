import os
import sys
import linecache
import functools
import io
from threading import Thread

from . import logger


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message='Time out'):
    pass


def trace(func):  # pragma: no cover
    pass


# https://github.com/giampaolo/psutil/blob/master/psutil/_common.py
def memoize(func):
    """
    A simple memoize decorator for functions supporting (hashable)
    positional arguments.
    It also provides a cache_clear() function for clearing the cache:

    >>> @memoize
    ... def foo()
    ...     return 1
        ...
    >>> foo()
    1
    >>> foo.cache_clear()
    >>>
    """
    pass


# https://github.com/giampaolo/psutil/blob/master/psutil/_common.py
def memoize_when_activated(func):
    """
    A memoize decorator which is disabled by default. It can be
    activated and deactivated on request.
    For efficiency reasons it can be used only against class methods
    accepting no arguments.

    >>> class Foo:
    ...     @memoize
    ...     def foo(self)
    ...         print(1)
    ...
    >>> f = Foo()
    >>> # deactivated (default)
    >>> foo()
    1
    >>> foo()
    1
    >>>
    >>> # activated
    >>> foo.cache_activate()
    >>> foo()
    1
    >>> foo()
    >>> foo()
    >>>
    """
    pass


# https://github.com/requests/requests/blob/master/requests/utils.py
def super_len(obj):
    pass
