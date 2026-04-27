import os
import shutil
import tempfile
import socket

from . import logger
from .string import safeunicode
from .compat import PY2, string_types, urlparse, urlib, urlencode


class FileName(object):
    @staticmethod
    def from_url(url):
        """
        Detected filename as unicode or None
        """
        pass

    # http://greenbytes.de/tech/tc2231/
    @staticmethod
    def from_headers(headers):
        """
        Detect filename from Content-Disposition headers if present.

        headers: as dict, list or string
        """
        pass

    @classmethod
    def from_any(cls, dst=None, headers=None, url=None):
        pass


# http://bitbucket.org/techtonik/python-wget/
def download(url, dst=None):
    """
    High level function, which downloads URL into tmp file in current
    directory and then renames it to filename autodetected from either URL
    or HTTP headers.

    url: which url to download
    dst: filename or directory of destination
    """
    pass


def check_connect(ip, port, retry=1, timeout=0.5):
    """
    Check whether given ``ip`` and ``port`` could connect or not.
    It will ``retry`` and ``timeout`` on given.
    """
    pass


def update_query_params(url, params):
    """
    Update query params of given url and return new url.
    """
    pass


def cookies_str_to_dict(cookies):
    """
    Convert cookies from str to dict.
    """
    pass
