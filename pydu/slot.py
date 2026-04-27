from .compat import iteritems, izip


class SlotBase(object):
    """
    Base class for class using __slots__.
    If some args or kwargs are not given when initialize class,
    the value of them will be set with ``None``.
    """
    def __init__(self, *args, **kwargs):
        pass
