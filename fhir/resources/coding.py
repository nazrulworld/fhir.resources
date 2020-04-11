# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coding
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


from . import element


class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """

    resource_type = "Coding"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Symbol in syntax defined by the system.
        Type `str`. """

        self.display = None
        """ Representation defined by the system.
        Type `str`. """

        self.system = None
        """ Identity of the terminology system.
        Type `str`. """

        self.userSelected = None
        """ If this coding was chosen directly by the user.
        Type `bool`. """

        self.version = None
        """ Version of the system - if relevant.
        Type `str`. """

        super(Coding, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, False),
                ("display", "display", str, "string", False, None, False),
                ("system", "system", str, "uri", False, None, False),
                ("userSelected", "userSelected", bool, "boolean", False, None, False),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js
