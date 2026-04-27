import os
from contextlib import contextmanager


@contextmanager
def cd(path):
    """
    Context manager for cd the given path.
    """
    pass


def is_super_path(path1, path2):
    """
    Whether `path1` is the super path of `path2`.
    Note that if `path1` is same as `path2`, it's also regarded as
    the super path os `path2`.
    For instance "/", "/opt" and "/opt/test" are all the super paths of "/opt/test",
    while "/opt/t" is the super path of "/opt/test".
    """
    pass


def normjoin(path, *paths):
    """Join one or more path components intelligently and normalize it."""
    pass


def filename(path):
    """Return the filename without extension."""
    pass


def fileext(path):
    """
    Return the file extension.
    If file has not extension, return empty string.
    """
    pass
