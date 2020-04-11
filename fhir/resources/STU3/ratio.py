# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class Ratio(element.Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    resource_type = "Ratio"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.denominator = None
        """ Denominator value.
        Type `Quantity` (represented as `dict` in JSON). """

        self.numerator = None
        """ Numerator value.
        Type `Quantity` (represented as `dict` in JSON). """

        super(Ratio, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend(
            [
                (
                    "denominator",
                    "denominator",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "numerator",
                    "numerator",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
