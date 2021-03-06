# -*- coding: utf-8 -*-
"""HIP Transport Modes"""

from pcapkit.vendor.default import Vendor

__all__ = ['Transport']


class Transport(Vendor):
    """HIP Transport Modes"""

    FLAG = 'isinstance(value, int) and 0 <= value <= 3'
    LINK = 'https://www.iana.org/assignments/hip-parameters/transport-modes.csv'


if __name__ == "__main__":
    Transport()
