# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Range
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class Range(element.Element):
    """ Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """

    resource_type = "Range"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.high = None
        """ High limit.
        Type `Quantity` (represented as `dict` in JSON). """

        self.low = None
        """ Low limit.
        Type `Quantity` (represented as `dict` in JSON). """

        super(Range, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend(
            [
                ("high", "high", quantity.Quantity, "Quantity", False, None, False),
                ("low", "low", quantity.Quantity, "Quantity", False, None, False),
            ]
        )
        return js


try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
