# -*- coding: utf-8 -*-
"""Mobility Header Types - for the MH Type field in the Mobility Header"""

import csv
import re

from pcapkit.vendor.default import Vendor

__all__ = ['Packet']


class Packet(Vendor):
    """Mobility Header Types - for the MH Type field in the Mobility Header"""

    FLAG = 'isinstance(value, int) and 0 <= value <= 255'
    LINK = 'https://www.iana.org/assignments/mobility-parameters/mobility-parameters-1.csv'

    def process(self, data):
        reader = csv.reader(data)
        next(reader)  # header

        enum = list()
        miss = [
            "extend_enum(cls, 'Unassigned [%d]' % value, value)",
            'return cls(value)'
        ]
        for item in reader:
            long = item[1]
            rfcs = item[2]

            temp = list()
            for rfc in filter(None, re.split(r'\[|\]', rfcs)):
                if 'RFC' in rfc:
                    temp.append('[{} {}]'.format(rfc[:3], rfc[3:]))
                else:
                    temp.append('[{}]'.format(rfc))
            desc = " {}".format(''.join(temp)) if rfcs else ''

            split = long.split(' (', 1)
            if len(split) == 2:
                name = split[0]
                cmmt = " ({}".format(split[1])
            else:
                name, cmmt = long, ''

            code, _ = item[0], int(item[0])
            renm = self.rename(name, code, original=long)

            pres = "{}[{!r}] = {}".format(self.NAME, renm, code)
            sufs = '# {}{}'.format(desc, cmmt) if desc or cmmt else ''

            if len(pres) > 74:
                sufs = "\n{}{}".format(' '*80, sufs)

            enum.append('{}{}'.format(pres.ljust(76), sufs))
        return enum, miss


if __name__ == "__main__":
    Packet()
