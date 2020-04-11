# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Narrative
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


from . import element


class Narrative(element.Element):
    """ A human-readable formatted text, including images.
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
