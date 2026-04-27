# coding: utf-8
import locale
from .compat import text_type


preferredencoding = locale.getpreferredencoding()


def safeunicode(obj, encoding='utf-8'):
    """
    Converts any given object to unicode string.

        >>> safeunicode('hello')
        u'hello'
        >>> safeunicode(2)
        u'2'
        >>> safeunicode('\xe4\xb8\xad\xe6\x96\x87')
        u'中文'
    """
    pass


def safeencode(obj, encoding='utf-8'):
    """
    Converts any given object to encoded string (default: utf-8).

        >>> safestr('hello')
        'hello'
        >>> safestr(2)
        '2'
    """
    pass


iters = [list, tuple, set, frozenset]
class _hack(tuple): pass
iters = _hack(iters)
iters.__doc__ = """
A list of iterable items (like lists, but not strings). Includes whichever
of lists, tuples, sets, and Sets are available in this version of Python.
"""


def _strips(direction, text, remove):
    pass


def rstrips(text, remove):
    """
    removes the string `remove` from the right of `text`
        >>> rstrips('foobar', 'bar')
        'foo'
    """
    pass


def lstrips(text, remove):
    """
    removes the string `remove` from the left of `text`

        >>> lstrips('foobar', 'foo')
        'bar'
        >>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
        'BAZ'
        >>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
        'BARBAZ'

    """
    pass


def strips(text, remove):
    """
    removes the string `remove` from the both sides of `text`
        >>> strips('foobarfoo', 'foo')
        'bar'
    """
    pass


def common_prefix(l):
    """
    Return common prefix of the stings
        >>> common_prefix(['abcd', 'abc1'])
        'abc'
    """
    pass


def common_suffix(l):
    """
    Return common suffix of the stings
        >>> common_suffix(['dabc', '1abc'])
        'abc'
    """
    pass


def sort(s, reverse=False):
    """
    Sort given string by ascending order.
    If reverse is True, sorting given string by descending order.
    """
    pass
