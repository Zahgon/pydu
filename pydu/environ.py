import os
from contextlib import contextmanager
from pydu.list import tolist
from pydu.compat import iteritems


@contextmanager
def environ(**kwargs):
    """
    Context manager for updating one or more environment variables.

    Preserves the previous environment variable (if available) and
    recovers when exiting the context manager.

    If given variable_name=None, it means removing the variable from
    environment temporarily.
    """
    pass


@contextmanager
def path(append=None, prepend=None, replace=None):
    """
    Context manager for updating the PATH environment variable which
    appends, prepends or replaces the PATH with given string or
    a list of strings.
    """
    pass
