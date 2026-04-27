# coding: utf-8
import collections

try:
    # Python 3
    from collections.abc import Callable, Mapping, MutableMapping
except ImportError:
    # Python 2.7
    from collections import Callable, Mapping, MutableMapping

from .compat import PY2


class AttrDict(dict):
    """
    A AttrDict object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.

        >>> o = AttrDict(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'

    """

    def __getattr__(self, key):
        pass

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, key):
        pass

    def __repr__(self):
        pass


class CaseInsensitiveDict(MutableMapping):
    """
    A case-insensitive ``dict``-like object.
    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.
    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive:
        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True
    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.
    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    """

    def __init__(self, data=None, **kwargs):
        pass

    def __setitem__(self, key, value):
        # Use the lowercased key for lookups, but store the actual
        # key alongside the value.
        pass

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        pass

    def __eq__(self, other):
        pass

    # Copy is required
    def copy(self):
        pass

    def __repr__(self):
        pass


class LookupDict(dict):
    """
    Dictionary lookup object.
        d = LookupDict()
        print(d['key'])  # None
        d['key'] = 1
        print(d['key'])  # 1
    """

    def __init__(self, name=None):
        self.name = name
        super(LookupDict, self).__init__()

    def __getitem__(self, key):
        # We allow fall-through here, so values default to None
        pass


# https://stackoverflow.com/questions/6190331/can-i-do-an-ordered-default-dict-in-python
class OrderedDefaultDict(collections.OrderedDict):
    """
    Dictionary that remembers insertion order and has default value
    with default factory.

    The default factory is called without arguments to produce
    a new value when a key is not present, in `__getitem__` only.
    An `OrderedDefaultDict` compares equal to a `collections.defaultdict`
    with the same items. All remaining arguments are treated the same
    as if they were passed to the `defaultdict` constructor,
    including keyword arguments.
    """

    def __init__(self, default_factory=None, *args, **kwds):
        pass

    def __getitem__(self, key):
        pass

    def __missing__(self, key):
        pass

    def __reduce__(self):
        pass

    def copy(self):
        pass

    def __copy__(self):
        pass

    if PY2:
        def __deepcopy__(self, memo):
            pass
    else:
        def __deepcopy__(self, memo):
            pass

    def __repr__(self):
        pass


def attrify(obj):
    pass
