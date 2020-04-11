# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Reference
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class Reference(element.Element):
    """ A reference from one resource to another.
    """

    resource_type = "Reference"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.display = None
        """ Text alternative for the resource.
        Type `str`. """

        self.identifier = None
        """ Logical reference, when literal reference is not known.
        Type `Identifier` (represented as `dict` in JSON). """

        self.reference = None
        """ Literal reference, Relative, internal or absolute URL.
        Type `str`. """

        super(Reference, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend(
            [
                ("display", "display", str, "string", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                ("reference", "reference", str, "string", False, None, False),
            ]
        )
        return js


try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
