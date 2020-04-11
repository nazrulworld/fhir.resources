# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Money
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import element


class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """

    resource_type = "Money"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.currency = None
        """ ISO 4217 Currency Code.
        Type `str`. """

        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """

        super(Money, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend(
            [
                ("currency", "currency", str, "code", False, None, False),
                ("value", "value", float, "decimal", False, None, False),
            ]
        )
        return js
