# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import element


class Narrative(element.Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).

    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """

    resource_type = "Narrative"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.div = None
        """ Limited xhtml content.
        Type `str`. """

        self.status = None
        """ generated | extensions | additional | empty.
        Type `str`. """

        super(Narrative, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend(
            [
                ("div", "div", str, "xhtml", False, None, True),
                ("status", "status", str, "code", False, None, True),
            ]
        )
        return js
