import os
import sys
import stat
import shutil
import locale

from . import logger
from .platform import WINDOWS
from .compat import PY2, builtins


_openfiles = set()
_origin_open = builtins.open
if PY2:
    _origin_file = builtins.file

    class _trackfile(builtins.file):
        def __init__(self, *args):
            pass

        def close(self):
            pass


    def _trackopen(*args):
        pass
else:
    def _trackopen(*args, **kwargs):
        pass


class FileTracker(object):
    @staticmethod
    def track():
        pass

    @staticmethod
    def untrack():
        pass

    @staticmethod
    def get_openfiles():
        pass


def makedirs(path, mode=0o755, ignore_errors=False, exist_ok=False):
    """
    Create a leaf directory and all intermediate ones.

    Based on os.makedirs, but also supports ignore_errors which will
    ignore all errors raised by os.makedirs.
    """
    pass


def remove(path, ignore_errors=False, onerror=None):
    """
    Remove a file or directory.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is False and onerror is None, it attempts to set path as writeable and
    then proceed with deletion if path is read-only, or raise an exception
    if path is not read-only.
    """
    pass


def removes(paths, ignore_errors=False, onerror=None):
    """
    Remove a list of file and/or directory.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is False and onerror is None, an exception is raised.
    """
    pass


def open_file(path, mode='wb+', buffer_size=-1, ignore_errors=False):
    """
    Open a file, defualt mode 'wb+'.

    If path not exists, it will be created automatically.
    If ignore_errors is set, errors are ignored.
    """
    pass


def copy(src, dst, ignore_errors=False, follow_symlinks=True):
    """
    Copy data and mode bits ("cp src dst").

    Both the source and destination may be a directory.

    When copy a directory,which contains a symlink, If the optional
    symlinks flag is true, symbolic links in the source tree result
    in symbolic links in the destination tree; if it is false, the
    contents of the files pointed to by symbolic links are copied.
    If the file pointed by the symlink doesn't exist, an exception
    will be raise.

    When copy a file,if follow_symlinks is false and src is a symbolic
    link, a new symlink will be created instead of copying the file it
    points to,else the contents of the file pointed to by symbolic links
    is copied.

    If source and destination are the same file, a SameFileError will be
    raised.

    If ignore_errors is set, errors are ignored.
    """
    pass


def touch(path):
    """
    Open a file as write,and then close it.
    """
    pass


def chmod(path, mode, recursive=False):
    """
    Change permissions to the given mode.
    If `recursive` is True perform recursively.

        >>> chmod('/opt/sometest', 0o755)
        >>> oct(os.stat('/opt/sometest').st_mode)[-3:]
        755
    """
    pass


if PY2:
    # shutil.which from Python3
    def which(cmd, mode=os.F_OK | os.X_OK, path=None):
        """
        Given a command, mode, and a PATH string, return the path which
        conforms to the given mode on the PATH, or None if there is no such
        file.

        `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
        of os.environ.get("PATH"), or can be overridden with a custom search
        path.
        """
        pass
else:
    which = shutil.which


if WINDOWS:
    # For Windows system
    from ctypes import windll

    class chcp(object):
        """
        Context manager which sets the active code page number.
        It could also be used as function.
        """
        def __init__(self, code):
            pass

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def __repr__(self):
            pass
else:
    # For non Windows system
    def symlink(src, dst, overwrite=False, ignore_errors=False):
        """
        Create a symbolic link pointing to source named link_name.

        If dist is exist and overwrite is true,a new symlink will be created

        If ignore_errors is set, errors are ignored.
        """
        pass


    def link(src, dst, overwrite=False, ignore_errors=False):
        """
        Create a hard link pointing to source named link_name.

        If dist is exist and overwrite is true,a new symlink will be created

        If ignore_errors is set, errors are ignored.
        """
        pass


def preferredencoding():
    """
    Get best encoding for the system.
    """
    pass
