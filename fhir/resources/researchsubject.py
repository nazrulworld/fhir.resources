# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class ResearchSubject(domainresource.DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """

    resource_type = "ResearchSubject"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actualArm = None
        """ What path was followed.
        Type `str`. """

        self.assignedArm = None
        """ What path should be followed.
        Type `str`. """

        self.consent = None
        """ Agreement to participate in study.
        Type `FHIRReference` referencing `['Consent']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier for research subject in a study.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.individual = None
        """ Who is part of study.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.period = None
        """ Start and end of participation.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ candidate | eligible | follow-up | ineligible | not-registered |
        off-study | on-study | on-study-intervention | on-study-observation
        | pending-on-study | potential-candidate | screening | withdrawn.
        Type `str`. """

        self.study = None
        """ Study subject is part of.
        Type `FHIRReference` referencing `['ResearchStudy']` (represented as `dict` in JSON). """

        super(ResearchSubject, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend(
            [
                ("actualArm", "actualArm", str, "string", False, None, False),
                ("assignedArm", "assignedArm", str, "string", False, None, False),
                (
                    "consent",
                    "consent",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                (
                    "individual",
                    "individual",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                ("status", "status", str, "code", False, None, True),
                (
                    "study",
                    "study",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
