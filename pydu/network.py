import socket
import struct
import ctypes
import binascii
from contextlib import closing

from .platform import WINDOWS
from .string import safeencode, safeunicode
from .convert import hex2dec, dec2hex


# https://github.com/hickeroar/win_inet_pton/blob/master/win_inet_pton.py
if WINDOWS:
    class _sockaddr(ctypes.Structure):
        _fields_ = [("sa_family", ctypes.c_short),
                    ("__pad1", ctypes.c_ushort),
                    ("ipv4_addr", ctypes.c_byte * 4),
                    ("ipv6_addr", ctypes.c_byte * 16),
                    ("__pad2", ctypes.c_ulong)]


    WSAStringToAddressA = ctypes.windll.ws2_32.WSAStringToAddressA
    WSAAddressToStringA = ctypes.windll.ws2_32.WSAAddressToStringA


    def _win_inet_pton(address_family, ip_str):
        pass


    def _win_inet_ntop(address_family, packed_ip):
        pass


    socket.inet_pton = _win_inet_pton
    socket.inet_ntop = _win_inet_ntop


# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def dotted_netmask(mask):
    """
    Converts mask from /xx format to xxx.xxx.xxx.xxx
    Example: if mask is 24 function returns 255.255.255.0
    """
    pass


# http://en.wikipedia.org/wiki/Private_network
private_ipv4s = [
    ('10.0.0.0', 8),  # 10.0.0.0 - 10.255.255.255
    ('172.16.0.0', 12),  # 172.16.0.0 - 172.31.255.255
    ('192.168.0.0', 16),  # 192.168.0.0 - 192.168.255.255
]


# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def is_ipv4(ip):
    """
    Returns True if the IPv4 address ia valid, otherwise returns False.
    """
    pass


def is_ipv6(ip):
    """
    Returns True if the IPv6 address ia valid, otherwise returns False.
    """
    pass


def get_free_port():
    pass


# https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python
# https://stackoverflow.com/questions/11894717/python-convert-ipv6-to-an-integer
def ip2int(ip_str):
    """
    Convert ip to integer. Support IPV4 and IPV6.
    Raise `ValueError` if convert failed.
    """
    pass


# https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python
def int2ip(ip_int):
    """
    Convert integer to ip. Support IPV4 and IPV6.
    Raise `ValueError` if convert failed.
    """
    pass
