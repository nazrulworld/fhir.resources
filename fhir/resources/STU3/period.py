# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Period
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class Period(element.Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """

    resource_type = "Period"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.end = None
        """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.start = None
        """ Starting time with inclusive boundary.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(Period, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend(
            [
                ("end", "end", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("start", "start", fhirdate.FHIRDate, "dateTime", False, None, False),
            ]
        )
        return js


try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
