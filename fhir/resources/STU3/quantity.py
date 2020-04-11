# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Quantity
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


from . import element


class Quantity(element.Element):
    """ A measured or measurable amount.

    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    resource_type = "Quantity"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Coded form of the unit.
        Type `str`. """

        self.comparator = None
        """ < | <= | >= | > - how to understand the value.
        Type `str`. """

        self.system = None
        """ System that defines coded unit form.
        Type `str`. """

        self.unit = None
        """ Unit representation.
        Type `str`. """

        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """

        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, False),
                ("comparator", "comparator", str, "code", False, None, False),
                ("system", "system", str, "uri", False, None, False),
                ("unit", "unit", str, "string", False, None, False),
                ("value", "value", float, "decimal", False, None, False),
            ]
        )
        return js
