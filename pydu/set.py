# coding: utf-8
import collections


class OrderedSet(object):
    """
    A set which keeps the ordering of the inserted items.
    """

    def __init__(self, iterable=None):
        self.dict = collections.OrderedDict.fromkeys(iterable or ())

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def discard(self, item):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass

    def __bool__(self):
        pass

    def __nonzero__(self):
        pass

    def __len__(self):
        pass
