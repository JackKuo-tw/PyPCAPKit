# -*- coding: utf-8 -*-
"""ARP Hardware Types [RFC 826][RFC 5494]"""

from pcapkit.vendor.default import Vendor

__all__ = ['Hardware']


class Hardware(Vendor):
    """Hardware Types [RFC 826][RFC 5494]"""

    FLAG = 'isinstance(value, int) and 0 <= value <= 65535'
    LINK = 'https://www.iana.org/assignments/arp-parameters/arp-parameters-2.csv'


if __name__ == '__main__':
    Hardware()
