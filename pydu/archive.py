"""
Based on "python-archive" -- http://pypi.python.org/pypi/python-archive/
Copyright (c) 2010 Gary Wilson Jr. <gary.wilson@gmail.com> and contributors.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import os
import shutil
import stat
import tarfile
import zipfile

from . import logger
from .compat import string_types


class ArchiveException(Exception):
    """
    Base exception class for all archive errors.
    """


class UnrecognizedArchiveFormat(ArchiveException):
    """
    Error raised when passed file is not a recognized archive format.
    """


def extract(path, dst='', ext=''):
    """
    Unpack the tar or zip file at the specified path or file to the directory
    specified by to_path.
    """
    pass


class Archive(object):
    """
    The external API class that encapsulates an archive implementation.
    """
    def __init__(self, file, ext=''):
        """
        Arguments:
        * 'file' can be a string path to a file or a file-like object.
        * Optional 'ext' argument can be given to override the file-type
          guess that is normally performed using the file extension of the
          given 'file'.  Should start with a dot, e.g. '.tar.gz'.
        """
        self._archive = self._archive_cls(file, ext=ext)(file)

    @staticmethod
    def _archive_cls(file, ext=''):
        """
        Return the proper Archive implementation class, based on the file type.
        """
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def extract(self, dst=''):
        pass

    def list(self):
        pass

    def filenames(self):
        pass

    def close(self):
        pass


class BaseArchive(object):
    """
    Base Archive class.  Implementations should inherit this class.
    """
    @staticmethod
    def _copy_permissions(mode, filename):
        """
        If the file in the archive has some permissions (this assumes a file
        won't be writable/executable without being readable), apply those
        permissions to the unarchived file.
        """
        pass

    def split_leading_dir(self, path):
        pass

    def has_leading_dir(self, paths):
        """
        Returns true if all the paths have the same leading path name
        (i.e., everything is in one subdirectory in an archive)
        """
        pass

    def extract(self, dst):
        raise NotImplementedError(
            'subclasses of BaseArchive must provide an extract() method')

    def list(self):
        raise NotImplementedError(
            'subclasses of BaseArchive must provide a list() method')

    def filenames(self):
        """
        Return a list of the filenames contained in the archive.
        """
        raise NotImplementedError()

    def __del__(self):
        pass


class TarArchive(BaseArchive):

    def __init__(self, file):
        # tarfile's open uses different parameters for file path vs. file obj.
        pass

    def extract(self, dst):
        pass

    def list(self):
        pass

    def filenames(self):
        pass

    def close(self):
        pass


class ZipArchive(BaseArchive):

    def __init__(self, file):
        # ZipFile's 'file' parameter can be path (string) or file-like obj.
        self._archive = zipfile.ZipFile(file)

    def extract(self, dst):
        pass

    def list(self):
        pass

    def filenames(self):
        pass

    def close(self):
        pass


extension_map = {
    '.tar': TarArchive,
    '.tar.bz2': TarArchive,
    '.tar.gz': TarArchive,
    '.tgz': TarArchive,
    '.tz2': TarArchive,
    '.zip': ZipArchive,
}
