# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Element
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


from . import fhirabstractbase


class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """

    resource_type = "Element"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.extension = None
        """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

        self.id = None
        """ xml:id (or equivalent in JSON).
        Type `str`. """

        super(Element, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension

        js.extend(
            [
                (
                    "extension",
                    "extension",
                    extension.Extension,
                    "Extension",
                    True,
                    None,
                    False,
                ),
                ("id", "id", str, "string", False, None, False),
            ]
        )
        return js
