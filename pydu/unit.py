

BYTE_UNITS = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')


class Bytes(object):
    """
    Supply several methods dealing with bytes.
    """
    def __init__(self, bytes):
        self.bytes = bytes

    def convert(self, unit=None, multiple=1024):
        """
        Convert bytes with given ``unit``.
        If `unit` is None, convert bytes with suitable unit.
        Convert `multiple` is default to be 1024.
        """
        pass
