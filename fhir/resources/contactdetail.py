# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactDetail
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import element


class ContactDetail(element.Element):
    """ Contact information.

    Specifies contact information for a person or organization.
    """

    resource_type = "ContactDetail"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Name of an individual to contact.
        Type `str`. """

        self.telecom = None
        """ Contact details for individual or organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(ContactDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ContactDetail, self).elementProperties()
        js.extend(
            [
                ("name", "name", str, "string", False, None, False),
                (
                    "telecom",
                    "telecom",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
