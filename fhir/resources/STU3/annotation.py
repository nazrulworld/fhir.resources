# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Annotation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class Annotation(element.Element):
    """ Text node with attribution.

    A  text note which also  contains information about who made the statement
    and when.
    """

    resource_type = "Annotation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authorReference = None
        """ Individual responsible for the annotation.
        Type `FHIRReference` referencing `['Practitioner'], ['Patient'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.authorString = None
        """ Individual responsible for the annotation.
        Type `str`. """

        self.text = None
        """ The annotation  - text content.
        Type `str`. """

        self.time = None
        """ When the annotation was made.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend(
            [
                (
                    "authorReference",
                    "authorReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "author",
                    False,
                ),
                ("authorString", "authorString", str, "string", False, "author", False),
                ("text", "text", str, "string", False, None, True),
                ("time", "time", fhirdate.FHIRDate, "dateTime", False, None, False),
            ]
        )
        return js


try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
