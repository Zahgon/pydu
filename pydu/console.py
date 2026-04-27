import sys
import shutil

from .platform import WINDOWS, POSIX


if hasattr(shutil, 'get_terminal_size'):
    # Actually (80, 25) is the default size used by many terminal emulators
    def console_size(fallback=(80, 25)):
        pass
else:
    # http://bitbucket.org/techtonik/python-pager
    def console_size(fallback=(80, 25)):
        """
        For Windows, return (width, height) of available window area, fallback
        if no console is allocated.
        For POSIX system, return (width, height) of console terminal, fallback
        on IOError, i.e. when no console is allocated.
        For other system, return fallback.
        Fallback defaults to (80, 25) which is the default size used by many
        terminal emulators.
        """
        pass
