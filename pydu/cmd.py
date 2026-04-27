import os
import sys
import time
import signal
import subprocess
from subprocess import Popen, PIPE, STDOUT

from .platform import WINDOWS
from .compat import PY2

if PY2:
    class TimeoutExpired(Exception):
        """
        This exception is raised when the timeout expires while waiting for a
        child process.

        Attributes:
            cmd, output, stdout, stderr, timeout
        """
        def __init__(self, cmd, timeout, output=None, stderr=None):
            self.cmd = cmd
            self.timeout = timeout
            self.output = output
            self.stderr = stderr

        def __str__(self):
            pass

        @property
        def stdout(self):
            pass

        @stdout.setter
        def stdout(self, value):
            # There's no obvious reason to set this, but allow it anyway so
            # .stdout is a transparent alias for .output
            pass
else:
    TimeoutExpired = subprocess.TimeoutExpired


def run(cmd, shell=False, env=None, timeout=None, timeinterval=1):
    """
    Run cmd based on `subprocess.Popen` and return the tuple of `(returncode, stdout)`.
    Note, `stderr` is redirected to `stdout`. `shell` is same to parameter of `Popen`.
    If the process does not terminate after `timeout` seconds, a `TimeoutExpired`
    exception will be raised. `timeinterval` is workable when timeout is given
    on Python 2. It means process status checking interval.
    """
    pass


def run_with_en_env(cmd, shell=False, env=None, timeout=None, timeinterval=1):
    """
    Run cmd with English character sets environment, so that the output will
    be in English.
    Parameters are same with `run`.
    """
    pass


def terminate(pid):
    """
    Terminate process by given pid.
    On Windows, using Kernel32.TerminateProcess to kill.
    On Other platforms, using os.kill with signal.SIGTERM to kill.
    """
    pass


if PY2 and WINDOWS:
    # enable passing unicode arguments from command line in Python 2.x
    # https://stackoverflow.com/questions/846850/read-unicode-characters
    def cmdline_argv():
        """
        Uses shell32.GetCommandLineArgvW to get sys.argv as a list of Unicode
        strings.

        Versions 2.x of Python don't support Unicode in sys.argv on Windows,
        with the underlying Windows API instead replacing multi-byte characters
        with '?'.
        """
        pass
else:
    def cmdline_argv():
        pass
