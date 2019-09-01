# -*- coding: utf-8 -*-
# pylint: disable=unused-import
"""IPv6 constant enumerations."""

from pcapkit.const.ipv6.extension_header import ExtensionHeader as IPv6_ExtensionHeader
from pcapkit.const.ipv6.option import Option as IPv6_Option
from pcapkit.const.ipv6.qs_function import QS_Function as IPv6_QS_Function
from pcapkit.const.ipv6.router_alert import RouterAlert as IPv6_RouterAlert
from pcapkit.const.ipv6.routing import Routing as IPv6_Routing
from pcapkit.const.ipv6.seed_id import SeedID as IPv6_SeedID
from pcapkit.const.ipv6.tagger_id import TaggerID as IPv6_TaggerID

__all__ = ['IPv6_ExtensionHeader', 'IPv6_Option', 'IPv6_QS_Function', 'IPv6_RouterAlert', 'IPv6_Routing',
           'IPv6_SeedID', 'IPv6_TaggerID']
