import functools
from pydu.compat import PY2


def boolean(obj):
    """
    Convert obj to a boolean value.
    If obj is string, obj will converted by case-insensitive way:
        * convert `yes`, `y`, `on`, `true`, `t`, `1` to True
        * convert `no`, `n`, `off`, `false`, `f`, `0` to False
        * raising TypeError if other values passed
    If obj is non-string, obj will converted by bool(obj).
    """
    pass


##########################################################################
# Convert number from one base(2, 8, 10, 16) to another base(2, 8, 10, 16)
##########################################################################
_oct_index = 1 if PY2 else 2


def _rstrip_L(func):
    pass


# binary to octal, decimal and hexadecimal
@_rstrip_L
def bin2oct(x):
    """
    Convert binary string to octal string.
    For instance: '1001' -> '11'
    """
    pass


def bin2dec(x):
    """
    Convert binary string to decimal number.
    For instance: '11' -> 3
    """
    pass


@_rstrip_L
def bin2hex(x):
    """
    Convert binary string to hexadecimal string.
    For instance: '11010' -> '1a'
    """
    pass


# octal to binary, decimal and hexadecimal
@_rstrip_L
def oct2bin(x):
    """
    Convert octal string to binary string.
    For instance: '11' -> '1001'
    """
    pass


def oct2dec(x):
    """
    Convert octal string to decimal number.
    For instance: '11' -> 9
    """
    pass


@_rstrip_L
def oct2hex(x):
    """
    Convert octal string to hexadecimal string.
    For instance: '32' -> '1a'
    """
    pass


# decimal to binary, octal and hexadecimal
@_rstrip_L
def dec2bin(x):
    """
    Convert decimal number to binary string.
    For instance: 3 -> '11'
    """
    pass


@_rstrip_L
def dec2oct(x):
    """
    Convert decimal number to octal string.
    For instance: 9 -> '11'
    """
    pass


@_rstrip_L
def dec2hex(x):
    """
    Convert decimal number to hexadecimal string.
    For instance: 26 -> '1a'
    """
    pass


# hexadecimal to binary, octal and decimal
@_rstrip_L
def hex2bin(x):
    """
    Convert hexadecimal string to binary string.
    For instance: '1a' -> '11010'
    """
    pass


@_rstrip_L
def hex2oct(x):
    """
    Convert hexadecimal string to octal string.
    For instance: '1a' -> '32'
    """
    pass


def hex2dec(x):
    """
    Convert hexadecimal string to decimal number.
    For instance: '1a' -> 26
    """
    pass
