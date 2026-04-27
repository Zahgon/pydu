from __future__ import absolute_import

import inspect

from .compat import PY2


def getargspec(func):
    """
    Get the names and default values of a function's parameters.

    A tuple of four things is returned: (args, varargs, keywords, defaults).
    'args' is a list of the argument names, including keyword-only argument names.
    'varargs' and 'keywords' are the names of the * and ** parameters or None.
    'defaults' is an n-tuple of the default values of the last n parameters.
    """
    pass


def get_func_args(func):
    """
    Return a list of the argument names. Arguments such as
    *args and **kwargs are not included.
    """
    pass


def get_func_full_args(func):
    """
    Return a list of (argument name, default value) tuples. If the argument
    does not have a default value, omit it in the tuple. Arguments such as
    *args and **kwargs are also included.
    """
    pass


def func_accepts_kwargs(func):
    """
    Check whether or not the func accepts kwargs.
    """
    pass


def func_accepts_var_args(func):
    """
    Check whether or not the func accepts var args.
    """
    pass


def func_supports_parameter(func, parameter):
    """
    Check whether or the func supports the given parameter.
    """
    pass


def func_has_no_args(func):
    """
    Check whether or not the func has any args.
    """
    pass
