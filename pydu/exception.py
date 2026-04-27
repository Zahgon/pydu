import contextlib
from functools import wraps
from .compat import PY2


if PY2:
    @contextlib.contextmanager
    def ignore(*exceptions):
        pass
else:
    ignore = contextlib.suppress


def default_if_except(exception_clses, default=None):
    """
    A exception decorator which excepts given exceptions and
    return default value.
    """
    pass
